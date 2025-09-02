document.addEventListener('DOMContentLoaded', function() {
    const toggle = document.getElementById('mode-toggle');

    function setInitialTheme() {
        const prefersLight = window.matchMedia('(prefers-color-scheme: light)').matches;
        if (prefersLight) {
            document.body.classList.add('light-mode');
            toggleIcon('sun');
        } else {
            document.body.classList.remove('light-mode');
            toggleIcon('moon');
        }
    }

    function toggleIcon(mode) {
        const icon = toggle.querySelector('i');
        if (mode === 'sun') {
            icon.classList.remove('fa-moon');
            icon.classList.add('fa-sun');
        } else {
            icon.classList.remove('fa-sun');
            icon.classList.add('fa-moon');
        }
    }

    function loadParticles(isLight) {
        particlesJS('particles-js', {
            particles: {
                number: { value: 80, density: { enable: true, value_area: 800 } },
                color: { value: isLight ? '#2563eb' : '#ffffff' },
                shape: { type: 'circle' },
                opacity: { value: isLight ? 0.7 : 0.5, random: false },
                size: { value: isLight ? 4 : 3, random: true },
                line_linked: {
                    enable: true,
                    distance: 140,
                    color: isLight ? '#60a5fa' : '#00fff7',
                    opacity: isLight ? 0.6 : 0.4,
                    width: isLight ? 2 : 1
                },
                move: { enable: true, speed: 6, direction: 'none', random: false, straight: false, out_mode: 'out', bounce: false }
            },
            interactivity: {
                detect_on: 'canvas',
                events: { onhover: { enable: true, mode: 'repulse' }, onclick: { enable: true, mode: 'push' }, resize: true },
                modes: { repulse: { distance: 200, duration: 0.4 }, push: { particles_nb: 4 } }
            },
            retina_detect: true
        });
    }

    setInitialTheme();
    loadParticles(document.body.classList.contains('light-mode'));

    toggle.addEventListener('click', () => {
        document.body.classList.toggle('light-mode');
        const isLight = document.body.classList.contains('light-mode');
        toggleIcon(isLight ? 'sun' : 'moon');
        // Animate progress bars from 0 to their percentage on theme switch
        document.querySelectorAll('.progress-bar').forEach(bar => {
            const percent = bar.textContent.match(/\d+/) ? bar.textContent.match(/\d+/)[0] : '0';
            bar.style.width = '0';
            setTimeout(() => {
                bar.style.width = percent + '%';
            }, 150);
        });
        // Reload particles with new theme
        document.getElementById('particles-js').innerHTML = '';
        setTimeout(() => loadParticles(isLight), 50);
    });

    // Initialize particles.js (techie background particles)
    particlesJS('particles-js', {
        particles: {
            number: { value: 80, density: { enable: true, value_area: 800 } },
            color: { value: '#ffffff' },
            shape: { type: 'circle' },
            opacity: { value: 0.5, random: false },
            size: { value: 3, random: true },
            line_linked: { enable: true, distance: 150, color: '#ffffff', opacity: 0.4, width: 1 },
            move: { enable: true, speed: 6, direction: 'none', random: false, straight: false, out_mode: 'out', bounce: false }
        },
        interactivity: {
            detect_on: 'canvas',
            events: { onhover: { enable: true, mode: 'repulse' }, onclick: { enable: true, mode: 'push' }, resize: true },
            modes: { repulse: { distance: 200, duration: 0.4 }, push: { particles_nb: 4 } }
        },
        retina_detect: true
    });
});