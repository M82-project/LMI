import matplotlib.pyplot as plt
import numpy as np

# Données
phases = {
    "Détecter": {
        "TA0011": ["TE0111", "TE0112"],
        "TA0012": ["TE0121", "TE0122"],
        "TA0013": ["TE0131", "TE0132"],
        "TA0014": ["TE0141", "TE0142", "TE0143"],
        "TA0015": ["TE0151", "TE0152"]
    },
    "Informer": {
        "TA0021": ["TE0211", "TE0212", "TE0213"],
        "TA0022": ["TE0221"],
        "TA0023": ["TE0231", "TE0232"],
        "TA0024": ["TE0241", "TE0242"],
        "TA0025": ["TE00251"],
        "TA0026": ["TE0261"]
    },
    "Mémoriser": {
        "TA0031": ["TE0312", "TE0313", "TE0314", "TE0315"],
        "TA0032": ["TE0321", "TE0322", "TE0323"],
        "TA0033": ["TE0331", "TE0332", "TE0333"]
    },
    "Agir": {
        "TA0041": ["TE0411", "TE0412", "TE0413"],
        "TA0042": ["TE0421", "TE0422"],
        "TA0043": ["TE0431", "TE0432", "TE0433"]
    }
}

# Créer un graphique circulaire
fig, ax = plt.subplots(figsize=(20, 20), subplot_kw={'projection': 'polar'})

# Angles pour chaque phase, en commençant par "Détecter" en haut
phase_angles = np.linspace(0, 2 * np.pi, len(phases), endpoint=False)
phase_angles = np.roll(phase_angles, shift=-1)  # Rotation pour placer "Détecter" en haut

# Dessiner chaque phase
for i, (phase, tactics) in enumerate(phases.items()):
    angle = phase_angles[i]
    ax.plot([angle, angle], [0, 1], color='gray', lw=2)
    ax.text(angle, 1, phase, color='black', ha='center', va='center', fontsize=16, fontweight='bold')

    # Angles pour chaque tactique dans la phase, avec espacement accru
    num_tactics = len(tactics)
    tactic_angles = np.linspace(angle - np.pi/8, angle + np.pi/8, num_tactics)

    for j, (tactic, techniques) in enumerate(tactics.items()):
        tactic_angle = tactic_angles[j]
        ax.plot([angle, tactic_angle], [1, 2], color='blue', lw=2)
        ax.text(tactic_angle, 2, tactic, color='blue', ha='center', va='center', fontsize=14)

        # Angles pour chaque technique associée à la tactique, avec espacement accru
        num_techniques = len(techniques)
        technique_angles = np.linspace(tactic_angle - np.pi/16, tactic_angle + np.pi/16, num_techniques)

        for k, technique in enumerate(techniques):
            technique_angle = technique_angles[k]
            ax.plot([tactic_angle, technique_angle], [2, 3], color='green', lw=1, ls='dotted')
            ax.text(technique_angle, 3, technique, color='green', ha='center', va='center', fontsize=12)

ax.set_yticklabels([])
ax.set_xticklabels([])
ax.set_title("Représentation des Phases, Tactiques et Techniques", va='bottom', fontsize=18)
plt.show()
