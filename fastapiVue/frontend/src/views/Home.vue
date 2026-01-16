<script setup>
import { ref } from 'vue'

// Données du menu
const navLinks = ref([
  { text: 'Accueil', url: '#' },
  { text: 'Tournois', url: '#' },
  { text: 'Jeux', url: '#' },
  { text: 'Classements', url: '#' }
])

// Données des tournois
const featuredTournaments = ref([
  {
    id: 1,
    gameName: 'VALORANT',
    title: 'Weekly Spike Clash #42',
    date: '24 Oct, 20:00',
    format: '5v5',
    imageUrl: 'https://images.unsplash.com/photo-1624138784614-87fd1b6528f8?ixlib=rb-4.0.3&auto=format&fit=crop&w=800&q=80',
    badgeStyle: null 
  },
  {
    id: 2,
    gameName: 'LEAGUE OF LEGENDS',
    title: "Summoner's Rift Cup",
    date: '26 Oct, 14:00',
    format: '5v5',
    imageUrl: 'https://images.unsplash.com/photo-1560419015-7c427e8ae5ba?ixlib=rb-4.0.3&auto=format&fit=crop&w=800&q=80',
    badgeStyle: null
  },
  {
    id: 3,
    gameName: 'ROCKET LEAGUE',
    title: 'Nitro Doubles Championship',
    date: '28 Oct, 19:00',
    format: '2v2',
    imageUrl: 'https://images.unsplash.com/photo-1509198397868-475647b2a1e5?ixlib=rb-4.0.3&auto=format&fit=crop&w=800&q=80',
    badgeStyle: { backgroundColor: '#9b59b6' } // Violet
  }
])
</script>

<template>
  <div class="home-container">
    <header class="main-header">
        <router-link to="/" class="logo-container">
            <div class="logo-icon"></div>
            NEXUS ARENA
        </router-link>

        <nav>
            <ul class="nav-links">
                <li v-for="(link, index) in navLinks" :key="index">
                  <a :href="link.url">{{ link.text }}</a>
                </li>
            </ul>
        </nav>

        <div class="auth-buttons">
            <button class="btn btn-outline">Connexion</button>
            <button class="btn btn-primary">S'inscrire</button>
        </div>
    </header>

    <main>
        <section class="hero">
            <div class="hero-content">
                <h1>Let's go!<br>Dominez la compétition</h1>
                <p>La plateforme ultime pour créer, gérer et rejoindre des tournois esport. Prouvez votre valeur et grimpez au classement.</p>
                <button class="btn btn-primary size-lg">Trouver un tournoi</button>
            </div>
        </section>

        <section class="featured-section">
            <h2 class="section-title">Tournois <span>À la une</span></h2>
            
            <div class="tournament-grid">
                <div v-for="tourney in featuredTournaments" :key="tourney.id" class="tournament-card">
                    <div class="card-image" :style="{ backgroundImage: `url(${tourney.imageUrl})` }">
                        <span class="game-badge" :style="tourney.badgeStyle ? tourney.badgeStyle : ''">
                          {{ tourney.gameName }}
                        </span>
                    </div>
                    <div class="card-content">
                        <h3>{{ tourney.title }}</h3>
                        <div class="card-info">
                            <span>📅 {{ tourney.date }}</span>
                            <span>👥 {{ tourney.format }}</span>
                        </div>
                        <button class="btn btn-outline full-width">Voir les détails</button>
                    </div>
                </div>
            </div>
        </section>
    </main>

    <footer>
        <p>© 2023 Nexus Arena - Projet étudiant. Tous droits réservés.</p>
    </footer>
  </div>
</template>

<style scoped>
/* Import Police */
@import url('https://fonts.googleapis.com/css2?family=Montserrat:wght@400;700;900&display=swap');

.home-container {
    --bg-dark: #0a0e17;
    --bg-card: #16213e;
    --accent-primary: #00d4ff;
    --accent-secondary: #9b59b6;
    --text-light: #ffffff;
    --text-gray: #b3b3b3;

    font-family: 'Montserrat', sans-serif;
    background-color: var(--bg-dark);
    color: var(--text-light);
    width: 100%;
    min-height: 100vh;
}

/* Header */
.main-header {
    display: flex;
    justify-content: space-between;
    align-items: center;
    padding: 20px 5%;
    background-color: rgba(10, 14, 23, 0.95);
    position: sticky;
    top: 0;
    z-index: 100;
    border-bottom: 1px solid rgba(255,255,255,0.1);
}

.logo-container {
    display: flex;
    align-items: center;
    font-weight: 900;
    font-size: 1.5rem;
    letter-spacing: 1px;
    color: var(--text-light);
    text-decoration: none;
}

.logo-icon {
    width: 40px;
    height: 40px;
    background: linear-gradient(45deg, var(--accent-primary), var(--accent-secondary));
    clip-path: polygon(20% 0%, 0% 20%, 30% 50%, 0% 80%, 20% 100%, 50% 70%, 80% 100%, 100% 80%, 70% 50%, 100% 20%, 80% 0%, 50% 30%);
    margin-right: 10px;
}

.nav-links {
    display: flex;
    gap: 30px;
    list-style: none;
    margin: 0;
    padding: 0;
}

.nav-links a {
    color: var(--text-light);
    text-decoration: none;
    transition: color 0.3s;
    font-weight: 700;
}

.nav-links a:hover {
    color: var(--accent-primary);
}

.auth-buttons {
    display: flex;
    gap: 15px;
}

/* Boutons */
.btn {
    padding: 10px 24px;
    border-radius: 4px;
    font-weight: 700;
    text-transform: uppercase;
    cursor: pointer;
    transition: all 0.3s ease;
    border: none;
    font-family: 'Montserrat', sans-serif;
}

.btn.size-lg {
    padding: 15px 40px;
    font-size: 1.1rem;
}

.btn.full-width {
    width: 100%;
}

.btn-primary {
    background: linear-gradient(45deg, var(--accent-primary), var(--accent-secondary));
    color: var(--bg-dark);
    box-shadow: 0 4px 15px rgba(0, 212, 255, 0.4);
}

.btn-primary:hover {
    transform: translateY(-2px);
    box-shadow: 0 6px 20px rgba(0, 212, 255, 0.6);
}

.btn-outline {
    background: transparent;
    border: 2px solid var(--accent-primary);
    color: var(--accent-primary);
}

.btn-outline:hover {
    background: var(--accent-primary);
    color: var(--bg-dark);
}

/* Hero */
.hero {
    height: 80vh;
    display: flex;
    align-items: center;
    justify-content: center;
    text-align: center;
    padding: 0 20px;
    background: 
        radial-gradient(circle at center, rgba(0, 212, 255, 0.15) 0%, rgba(10, 14, 23, 0.9) 70%),
        linear-gradient(rgba(10, 14, 23, 0.5), rgba(10, 14, 23, 0.95)),
        url('https://images.unsplash.com/photo-1542751371-adc38448a05e?ixlib=rb-4.0.3&auto=format&fit=crop&w=1920&q=80') no-repeat center center/cover;
}

.hero-content h1 {
    font-size: 4rem;
    font-weight: 900;
    margin-bottom: 20px;
    text-transform: uppercase;
    line-height: 1.1;
    background: linear-gradient(to right, var(--text-light), var(--accent-primary));
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    background-clip: text;
}

.hero-content p {
    font-size: 1.2rem;
    color: var(--text-gray);
    max-width: 650px;
    margin: 0 auto 40px auto;
}

/* Section Featured */
.featured-section {
    padding: 80px 5%;
}

.section-title {
    font-size: 2.5rem;
    margin-bottom: 50px;
    text-align: center;
    font-weight: 800;
}
.section-title span {
    color: var(--accent-primary);
}

.tournament-grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
    gap: 30px;
}

.tournament-card {
    background-color: var(--bg-card);
    border-radius: 12px;
    overflow: hidden;
    transition: transform 0.3s ease, border-color 0.3s ease;
    border: 1px solid rgba(255, 255, 255, 0.05);
    display: flex;
    flex-direction: column;
}

.tournament-card:hover {
    transform: translateY(-7px);
    border-color: var(--accent-primary);
}

.card-image {
    height: 180px;
    width: 100%;
    background-size: cover;
    background-position: center;
    position: relative;
}

.game-badge {
    position: absolute;
    top: 10px;
    left: 10px;
    background: var(--accent-primary);
    color: var(--bg-dark);
    padding: 5px 10px;
    font-size: 0.8rem;
    font-weight: 800;
    border-radius: 4px;
    text-transform: uppercase;
}

.card-content {
    padding: 20px;
    flex-grow: 1;
    display: flex;
    flex-direction: column;
}

.card-content h3 {
    font-size: 1.3rem;
    margin-bottom: 10px;
    font-weight: 700;
}

.card-info {
    display: flex;
    justify-content: space-between;
    color: var(--text-gray);
    font-size: 0.9rem;
    margin-bottom: 20px;
}

.card-content .btn {
    margin-top: auto;
}

/* Footer */
footer {
    background: #05080f;
    padding: 40px 5%;
    text-align: center;
    color: var(--text-gray);
    margin-top: auto;
    border-top: 1px solid rgba(255,255,255,0.05);
}

/* Mobile */
@media (max-width: 768px) {
    .main-header {
        flex-direction: column;
        gap: 15px;
        padding: 15px;
    }
    .nav-links {
        flex-wrap: wrap;
        justify-content: center;
        gap: 15px;
    }
    .hero-content h1 {
        font-size: 2.5rem;
    }
}
</style>