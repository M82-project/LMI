import matplotlib.pyplot as plt
import numpy as np

# Données
data = {
    "TA01": {"name": "Plan Strategy", "children": ["T0074"]},
    "TA02": {"name": "Plan Objectives", "children": ["T0002", "T0066", "T0075", "T0076", "T0077", "T0079"]},
    "TA13": {"name": "Target Audience Analysis", "children": ["T0072", "T0081"]},
    "TA14": {"name": "Develop Narratives", "children": ["T0003", "T0004", "T0022", "T0040", "T0068", "T0083"]},
    "TA06": {"name": "Develop Content", "children": ["T0019", "T0023", "T0084", "T0086", "T0087"]},
    "TA15": {"name": "Establish Social Assets", "children": ["T0090"]},
    "TA16": {"name": "Establish Legitimacy", "children": ["T0099"]},
    "TA07": {"name": "Select Channels and Affordances", "children": ["T0104", "T0112"]},
    "TA09": {"name": "Deliver Content", "children": ["T0115", "T0116"]},
    "TA11": {"name": "Persist in the Information Environment", "children": ["T0128", "T0129"]},
}

additional_details = {
    "T0075": ["T0075.001"],
    "T0072": ["T0072.001"],
    "T0081": ["T0081.003", "T0081.004", "T0081.005", "T0081.008"],
    "T0022": ["T0022.001", "T0022.002"],
    "T0023": ["T0023.001", "T0023.002"],
    "T0084": ["T0084.002", "T0084.003"],
    "T0086": ["T0086.003"],
    "T0087": ["T0087.002"],
    "T0090": ["T0090.001"],
    "T0099": ["T0099.002", "T0099.003", "T0099.004", "T0099.005", "T0099.006"],
    "T0104": ["T0104.001"],
    "T0128": ["T0128.001", "T0128.004"],
    "T0129": ["T0129.002"],
}

# Créer un graphique circulaire
fig, ax = plt.subplots(figsize=(20, 20), subplot_kw={'projection': 'polar'})

# Nombre de tactiques
num_tactics = len(data)

# Angles pour chaque tactique
angles = np.linspace(0, 2 * np.pi, num_tactics, endpoint=False)

# Tracer les tactiques au centre
for i, (tactic, info) in enumerate(data.items()):
    angle = angles[i]
    ax.plot([angle, angle], [0, 2], color='blue', lw=2)
    ax.text(angle, 2, info["name"], color='blue', ha='center', va='center', fontsize=14)

    # Tracer les techniques autour de la périphérie
    num_techniques = len(info["children"])
    technique_angles = np.linspace(angle - np.pi/10, angle + np.pi/10, num_techniques)
    for j, technique in enumerate(info["children"]):
        tech_angle = technique_angles[j]
        ax.plot([angle, tech_angle], [2, 3], color='gray', lw=1, ls='dotted')
        ax.text(tech_angle, 3, technique, color='green', ha='center', va='center', fontsize=12)

        # Tracer les sous-techniques si elles existent
        if technique in additional_details:
            num_sub_techniques = len(additional_details[technique])
            sub_technique_angles = np.linspace(tech_angle - np.pi/20, tech_angle + np.pi/20, num_sub_techniques)
            for k, sub_technique in enumerate(additional_details[technique]):
                sub_angle = sub_technique_angles[k]
                ax.plot([tech_angle, sub_angle], [3, 4], color='gray', lw=1, ls='dotted')
                ax.text(sub_angle, 4, sub_technique, color='red', ha='center', va='center', fontsize=11)

ax.set_yticklabels([])
ax.set_xticklabels([])
ax.set_title("Circular Representation of Tactics, Techniques & Procedures", va='bottom', fontsize=16)
plt.show()
