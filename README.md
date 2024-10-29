
$$ {\Huge \color{#D969E0} \textsf{Goal: To be open source, and to video chat with AI!}} $$



Open source AI companion with voice to voice (check), text to text (check), and video generation (eventually), with emotional recognition (eventually)!

## Setup

1. Create a .env file in both templates/root folders
2. For .env in `templates/`, add `ELEVEN_LABS_API_KEY` and `OPENAI_API_KEY`
3. For .env in root, add `OPENAI_API_KEY`,
`HUME_API_KEY`,
`FAL_KEY`
`ELEVEN_LABS_API_KEY`,
`VOICE_ID`. The voice ID I am using is `'2iu0hNtfcnLuxyndzwxv'`


## Todos

### Code/Features:

1. Add capability to generate who you are speaking with (likely FLUX.1 AI photorealistic photo)
2. Add video to generations from Runway 3/Kling or comparable source (maybe add multiple layers? background layer/middleground layer/ foreground with companion)
3. Filter punctuation for code/code should not be spoken by AI model and instead should be skipped
4. Add Hume AI integration for emotional capabilities
5. Chunk and sequence long text into shorter text for audio generations, speeding up generation time and not taking like 2 minutes before it starts talking


### Documentation/Structure:

1. Make setup instructions more thorough
2. Create guide for contributing
3. Make Roadmap
4. Reduce bloat code in app.py and chat.css   
5. Add comments to code for better readability and chat.css

# What's done
1. Integration with ElevenLabs voice + OpenAI gpt4o!
2. Voice-to-text when hlding space bar
3. Basic and smooth UI
