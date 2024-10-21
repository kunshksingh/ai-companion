// Get elements
const seedModal = document.getElementById('seedModal');
const expandSeedBtn = document.getElementById('expandSeed');
const closeModalBtn = document.getElementById('closeModal');
const templateTab = document.getElementById('templateTab');
const customTab = document.getElementById('customTab');
const templateContent = document.getElementById('templateContent');
const customContent = document.getElementById('customContent');
const seedForm = document.getElementById('seedForm');
const customPromptForm = document.getElementById('customPromptForm');
const emotionIntensityInput = seedForm.emotion_intensity;
const emotionIntensityValueDisplay = document.getElementById('emotionIntensityValue');

// Open Modal
function openModal() {
  seedModal.classList.remove('hidden');
  seedModal.classList.add('flex');
  // Animation
  setTimeout(() => {
    seedModal.children[0].classList.remove('scale-95');
    seedModal.children[0].classList.add('scale-100');
  }, 10);
}

// Close Modal
function closeModal() {
  // Animation
  seedModal.children[0].classList.remove('scale-100');
  seedModal.children[0].classList.add('scale-95');
  setTimeout(() => {
    seedModal.classList.add('hidden');
    seedModal.classList.remove('flex');
  }, 200);
}

// Close Modal When Clicking Outside
function closeModalOnOutsideClick(event) {
  if (event.target === seedModal) {
    closeModal();
  }
}

// Event Listeners
expandSeedBtn.addEventListener('click', openModal);
closeModalBtn.addEventListener('click', closeModal);

// Toggle between Template and Custom Prompt
templateTab.addEventListener('click', () => {
  templateTab.classList.add('text-white', 'font-bold');
  templateTab.classList.remove('text-purple-300');
  customTab.classList.remove('text-white', 'font-bold');
  customTab.classList.add('text-purple-300');
  templateContent.classList.remove('hidden');
  customContent.classList.add('hidden');
});

customTab.addEventListener('click', () => {
  customTab.classList.add('text-white', 'font-bold');
  customTab.classList.remove('text-purple-300');
  templateTab.classList.remove('text-white', 'font-bold');
  templateTab.classList.add('text-purple-300');
  customContent.classList.remove('hidden');
  templateContent.classList.add('hidden');
});

// Update Emotion Intensity Display
emotionIntensityInput.addEventListener('input', function() {
  emotionIntensityValueDisplay.textContent = `${emotionIntensityInput.value}%`;
});

// Handle Seed Form Submission
seedForm.addEventListener('submit', async function(e) {
  e.preventDefault();

  // Collect form data
  const formData = new FormData(seedForm);
  const data = {};
  formData.forEach((value, key) => {
    data[key] = value;
  });

  data.nsfw = data.nsfw ? true : false;
  data.emotion_intensity = parseInt(data.emotion_intensity);

  // Get viewport dimensions
  const width = window.innerWidth;
  const height = window.innerHeight - (window.innerHeight * 0.14);

  // Add dimensions to data
  data.width = width;
  data.height = height;

  // Send POST request
  try {
    const response = await fetch('/video_feed', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify(data),
    });

    const result = await response.json();

    if (result.image_url) {
      // Set the generated image as the background of the chat container
      const chatContainer = document.getElementById('messages');
      chatContainer.style.backgroundImage = `url(${result.image_url})`;
    }

    // Close the modal
    closeModal();

  } catch (error) {
    console.error('Error fetching seed image:', error);
  }
});

// Handle Custom Prompt Form Submission
customPromptForm.addEventListener('submit', async function(e) {
  e.preventDefault();

  const customPrompt = customPromptForm.custom_prompt.value;

  // Get viewport dimensions
  const width = window.innerWidth;
  const height = window.innerHeight - (window.innerHeight * 0.14);

  const data = {
    custom_prompt: customPrompt,
    width: width,
    height: height
  };

  // Send POST request
  try {
    const response = await fetch('/video_feed', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify(data),
    });

    const result = await response.json();

    if (result.image_url) {
      // Set the generated image as the background of the chat container
      const chatContainer = document.getElementById('messages');
      chatContainer.style.backgroundImage = `url(${result.image_url})`;
    }

    // Close the modal
    closeModal();

  } catch (error) {
    console.error('Error fetching seed image:', error);
  }
});

// Display existing image on load if it exists
window.onload = function() {
  const chatContainer = document.getElementById('messages');
  chatContainer.style.backgroundImage = "url('/static/img/image.jpg')";
};
