// Game state
let ingredientsAdded = 0;
const totalIngredients = 6;

// Ingredient icons mapping
const ingredientIcons = {
    'ia': '🤖',
    'ipd': '🏛️',
    'leman': '💡',
    'tech': '🚀',
    'education': '📚',
    'olivia': '💝'
};

// Initialize the game
function init() {
    document.getElementById('totalCount').textContent = totalIngredients;

    // Add click handlers to all ingredients
    const ingredients = document.querySelectorAll('.ingredient');
    ingredients.forEach(ingredient => {
        ingredient.addEventListener('click', handleIngredientClick);
    });
}

function handleIngredientClick(event) {
    const ingredient = event.currentTarget;
    const isAdded = ingredient.getAttribute('data-added') === 'true';

    // Prevent adding the same ingredient twice
    if (isAdded) {
        return;
    }

    // Get ingredient data
    const ingredientType = ingredient.getAttribute('data-ingredient');
    const icon = ingredientIcons[ingredientType];

    // Add animation to ingredient card
    ingredient.classList.add('adding');

    // Mark as added
    setTimeout(() => {
        ingredient.setAttribute('data-added', 'true');
        ingredient.classList.remove('adding');
    }, 600);

    // Add to cauldron
    addToCauldron(icon);

    // Update counter
    ingredientsAdded++;
    document.getElementById('progressCount').textContent = ingredientsAdded;

    // Make cauldron bubble
    const cauldron = document.getElementById('cauldron');
    cauldron.classList.add('bubbling');
    setTimeout(() => {
        cauldron.classList.remove('bubbling');
    }, 500);

    // Check if all ingredients are added
    if (ingredientsAdded === totalIngredients) {
        setTimeout(showCelebration, 1000);
    }
}

function addToCauldron(icon) {
    const cauldronContent = document.getElementById('cauldronContent');

    // Update fill level
    const fillPercentage = (ingredientsAdded + 1) / totalIngredients * 100;
    cauldronContent.style.height = fillPercentage + '%';

    // Add glow effect when filling
    cauldronContent.classList.add('filling');
    setTimeout(() => {
        cauldronContent.classList.remove('filling');
    }, 600);

    // Add ingredient icon to cauldron
    const ingredientElement = document.createElement('span');
    ingredientElement.className = 'ingredient-in-cauldron';
    ingredientElement.textContent = icon;
    cauldronContent.appendChild(ingredientElement);
}

function showCelebration() {
    const celebrationScreen = document.getElementById('celebrationScreen');
    celebrationScreen.classList.add('show');

    // Play celebration sound (optional - can be enabled if audio file is added)
    // const audio = new Audio('celebration.mp3');
    // audio.play();
}

function restartGame() {
    // Reset game state
    ingredientsAdded = 0;
    document.getElementById('progressCount').textContent = '0';

    // Reset ingredients
    const ingredients = document.querySelectorAll('.ingredient');
    ingredients.forEach(ingredient => {
        ingredient.setAttribute('data-added', 'false');
    });

    // Clear cauldron
    const cauldronContent = document.getElementById('cauldronContent');
    cauldronContent.innerHTML = '';
    cauldronContent.style.height = '0';

    // Hide celebration screen
    const celebrationScreen = document.getElementById('celebrationScreen');
    celebrationScreen.classList.remove('show');
}

// Prevent zoom on double tap for better mobile experience
let lastTouchEnd = 0;
document.addEventListener('touchend', function(event) {
    const now = Date.now();
    if (now - lastTouchEnd <= 300) {
        event.preventDefault();
    }
    lastTouchEnd = now;
}, false);

// Prevent pull-to-refresh
document.body.addEventListener('touchmove', function(event) {
    if (event.touches.length > 1) {
        event.preventDefault();
    }
}, { passive: false });

// Start the game when page loads
window.addEventListener('DOMContentLoaded', init);
