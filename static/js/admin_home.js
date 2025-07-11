 const menuToggle = document.getElementById('menuToggle');
        const navLinks = document.getElementById('navLinks');
        
        menuToggle.addEventListener('click', () => {
            navLinks.classList.toggle('active');
        });
        
        // Dynamic product counter (simulated - replace with real data)
        let count = 0;
        const targetCount = 127; // Replace with actual product count from your database
        const counterElement = document.getElementById('productCount');
        const counterInterval = setInterval(() => {
            if (count < targetCount) {
                count++;
                counterElement.textContent = count;
            } else {
                clearInterval(counterInterval);
            }
        }, 30);
        
        // Update copyright year
        document.getElementById('currentYear').textContent = new Date().getFullYear();
        
        // Simulate loading animation
        document.addEventListener('DOMContentLoaded', () => {
            const featureCards = document.querySelectorAll('.feature-card');
            featureCards.forEach((card, index) => {
                setTimeout(() => {
                    card.style.opacity = '1';
                }, 200 * index);
            });
        });