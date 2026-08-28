import time
import random
import numpy as np
from sklearn.ensemble import IsolationForest



# BRIQUE 1 : LE SIMULATEUR DE CAPTEUR MÉDICAL IOT

def generer_donnees_patient(mode_attaque=False):
    if not mode_attaque:
        pouls = random.randint(65, 85)  # Normal
        spo2 = random.randint(95, 100)  # Normal
    else:
        pouls = random.randint(180, 220)  # Attaque cyber
        spo2 = random.randint(40, 55)  # Attaque cyber
    return [pouls, spo2]



# BRIQUE 2 : GÉNÉRATION AUTOMATIQUE D'UN VRAI HISTORIQUE POUR L'IA

print("🤖 1. Génération de la base d'entraînement (200 dossiers patients sains)...")

# On génère 200 lignes de données 100% normales automatiquement
base_donnees_normales = [generer_donnees_patient(mode_attaque=False) for _ in range(200)]
base_donnees_normales = np.array(base_donnees_normales)

# Initialisation du modèle Isolation Forest avec un taux de contamination très faible (1%)
modele_ia = IsolationForest(contamination=0.01, random_state=42)
modele_ia.fit(base_donnees_normales)

print("✅ IA entraînée avec succès. Les faux positifs sont corrigés.\n")


# BRIQUE 3 : SURVEILLANCE RÉSEAU EN TEMPS RÉEL (RÉSILIENCE)

canal_reseau = "Wi-Fi Principal (Canal Hospitalier)"
print(f"📡 Connexion établie sur : {canal_reseau}")
print("🏥 Démarrage de la surveillance du patient...\n")

for cycle in range(1, 9):  # On simule 8 cycles d'envoi

    if cycle == 5:
        print("\n❌ [ALERTE SÉCURITÉ] : Un pirate intercepte le Wi-Fi et injecte des fausses trames...")
        donnee_actuelle = generer_donnees_patient(mode_attaque=True)
    else:
        donnee_actuelle = generer_donnees_patient(mode_attaque=False)

    # L'IA analyse la donnée
    prediction = modele_ia.predict([donnee_actuelle])

    print(f"[Cycle {cycle}] - Pouls: {donnee_actuelle[0]} bpm | SpO2: {donnee_actuelle[1]}% | Canal: {canal_reseau}")

    # Si l'IA détecte l'attaque (-1)
    if prediction == -1:
        print("⚠️  [ALERTE IA] : Données falsifiées détectées !")
        print("🛡️  [MÉCANISME ADAPTATIF] : Coupure du Wi-Fi compromis...")

        # Action de résilience
        canal_reseau = "Réseau Cellulaire de Secours 4G/5G"
        print(f"🔄 [RÉSILIENT] : Flux sécurisé et basculé sur : {canal_reseau}\n")

    time.sleep(1.5)

print("\n🏁 Fin de la simulation du prototype technique.")
