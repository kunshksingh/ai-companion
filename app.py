import os
from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
from decouple import config
from model import GPT_Engine  # Existing model functionality
from dotenv import load_dotenv
import requests
import fal_client
import json
import asyncio

load_dotenv()

ELEVEN_LABS_API_KEY = config('ELEVEN_LABS_API_KEY')
VOICE_ID = config('VOICE_ID')
FAL_API_KEY = os.getenv('FAL_KEY')

app = Flask(__name__)
CORS(app)

engine = GPT_Engine()

# Load system message from system.txt
with open("system.txt", "r") as file:
    system_message = file.read()

try:
    with open("seed.txt", "r") as file:
        seed = file.read()
    engine.add_message(system_message, message_role="system")
except: 
    print("No seed.txt file found - either make a seed.txt file and restart to generate video feed, or add in application")
    


@app.route('/')
def chat():
    return render_template('chat.html', api_key=ELEVEN_LABS_API_KEY, voiceid=VOICE_ID, speak=True)

@app.route('/reset', methods=["GET"])
def reset():
    engine.clear()
    return ""

@app.route('/sendmessage', methods=['POST'])
def send_message():
    message = request.json['out']
    engine.add_message(message)
    engine.generate_response()
    print(engine.top())
    return jsonify(engine.top())

# Video feed route using Fal.ai Flux.1
@app.route('/video_feed', methods=['POST'])
async def video_feed():
    global seed
    data = request.json

    # Extract width and height
    width = data.get('width')
    height = data.get('height')

    # Build the system prompt
    if 'custom_prompt' in data:
        system_prompt = data['custom_prompt']
    else:
        # Build the prompt from template inputs
        prompt = data.get('prompt', '')
        setting = data.get('setting', '')
        quality = data.get('quality', '')
        zoom = data.get('zoom', '')
        scene_mood = data.get('scene_mood', '')
        companion_emotion = data.get('companion_emotion', '')
        emotion_intensity = data.get('emotion_intensity', '')
        nsfw = data.get('nsfw', False)

        # Construct the system prompt

        if nsfw:
            prompt += " [NSFW]"
        system_prompt = f"{{prompt='{prompt}', setting='{setting}', quality='{quality}', zoom='{zoom}', mood='{scene_mood}', emotion='{companion_emotion}', emotion_intensity='{emotion_intensity}'}}"

    # Call Fal.ai Flux.1 model for image generation
    try:
        handler = await fal_client.submit_async(
            "fal-ai/flux/dev",
            arguments={
                "prompt": system_prompt,
                "image_size": {
                    "width": width,
                    "height": height
                },
                "num_inference_steps": 28,
                "guidance_scale": 3.5,
                "num_images": 1,
                "enable_safety_checker": 0
            },
        )
        result = await handler.get()

        image_url = result['images'][0]['url'] 

        img_data = requests.get(image_url).content
        with open('static/img/image.jpg', 'wb') as handler:
            handler.write(img_data)

        print("Image", image_url)
        return jsonify({"image_url": image_url})

    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
