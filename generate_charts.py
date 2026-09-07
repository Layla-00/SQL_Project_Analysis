import os
import matplotlib.pyplot as plt
import numpy as np

os.makedirs('visualizations', exist_ok=True)
plt.rcParams['font.sans-serif'] = 'DejaVu Sans'

# 1. purchases_by_channel.png
fig, ax = plt.subplots(figsize=(10, 6), dpi=600)
fig.patch.set_facecolor('#ffffff')
channels = ['Store', 'Web', 'Catalog']
purchases = [12970, 9150, 5963]
colors = ['#1a365d', '#2b6cb0', '#4299e1']
bars = ax.bar(channels, purchases, color=colors, width=0.45, zorder=3)
ax.set_title('Total Purchases by Channel', fontsize=18, fontweight='bold', pad=25, color='#0f172a')
ax.grid(axis='y', linestyle='--', alpha=0.35, color='#94a3b8', zorder=0)
for spine in ['top', 'right', 'left']:
    ax.spines[spine].set_visible(False)
ax.spines['bottom'].set_color('#cbd5e1')
ax.spines['bottom'].set_linewidth(1.5)
ax.set_xticks(range(len(channels)))
ax.set_xticklabels(channels, fontweight='bold', fontsize=13, color='#1e293b')
ax.tick_params(axis='x', pad=10)
ax.tick_params(axis='y', labelsize=11, colors='#64748b')
ax.yaxis.set_major_formatter('{x:,.0f}')
for bar in bars:
    yval = bar.get_height()
ax.text(bar.get_x() + bar.get_width()/2, yval + 280, f'{yval:,}', ha='center', va='bottom', fontweight='bold', fontsize=14, color='#0f172a')
ax.set_ylim(0, 15500)
plt.tight_layout()
plt.savefig('visualizations/purchases_by_channel.png', bbox_inches='tight', dpi=600)
plt.close()

# 2. campaign_response.png
fig, ax = plt.subplots(figsize=(8, 6.5), dpi=600)
fig.patch.set_facecolor('#ffffff')
sizes = [334, 1906]
labels = ['Responders\n334 (14.91%)', 'Non-Responders\n1,906 (85.09%)']
colors_donut = ['#1a365d', '#93c5fd']
wedges, texts = ax.pie(sizes, colors=colors_donut, startangle=90, counterclock=False, wedgeprops=dict(width=0.38, edgecolor='white', linewidth=3))
ax.text(0, 0.1, '2,240', ha='center', va='center', fontsize=22, fontweight='bold', color='#0f172a')
ax.text(0, -0.12, 'Total Customers', ha='center', va='center', fontsize=12, fontweight='bold', color='#64748b')
ax.set_title('Campaign Response Rate', fontsize=18, fontweight='bold', pad=20, color='#0f172a')
ax.legend(wedges, labels, loc="center left", bbox_to_anchor=(0.88, 0.5), frameon=False, fontsize=12)
plt.tight_layout()
plt.savefig('visualizations/campaign_response.png', bbox_inches='tight', dpi=600)
plt.close()

# 3. income_by_education.png
fig, ax = plt.subplots(figsize=(10, 6), dpi=600)
fig.patch.set_facecolor('#ffffff')
education = ['PhD', 'Master', 'Graduation', '2n Cycle', 'Basic']
income = [56.1, 52.9, 52.7, 47.6, 20.3]
colors_edu = ['#1a365d', '#2b6cb0', '#3182ce', '#4299e1', '#63b3ed']
bars1 = ax.barh(education, income, color=colors_edu, height=0.55, zorder=3)
ax.set_title('Average Income by Education Level', fontsize=18, fontweight='bold', pad=25, color='#0f172a')
ax.grid(axis='x', linestyle='--', alpha=0.35, color='#94a3b8', zorder=0)
for spine in ['top', 'right', 'left']:
    ax.spines[spine].set_visible(False)
ax.spines['bottom'].set_color('#cbd5e1')
ax.spines['bottom'].set_linewidth(1.5)
ax.set_yticks(range(len(education)))
ax.set_yticklabels(education, fontweight='bold', fontsize=13, color='#1e293b')
ax.tick_params(axis='y', pad=10)
ax.tick_params(axis='x', labelsize=11, colors='#64748b')
ax.xaxis.set_major_formatter('{x:.0f}K')
for bar in bars1:
    xval = bar.get_width()
ax.text(xval + 1.2, bar.get_y() + bar.get_height()/2, f'{xval:.1f}K', ha='left', va='center', fontweight='bold', fontsize=13, color='#0f172a')
ax.set_xlim(0, 68)
ax.invert_yaxis()
plt.tight_layout()
plt.savefig('visualizations/income_by_education.png', bbox_inches='tight', dpi=600)
plt.close()

# 4. digital_behavior.png
fig, ax = plt.subplots(figsize=(10, 6), dpi=600)
fig.patch.set_facecolor('#ffffff')
metrics = ['Avg Web Purchases', 'Avg Monthly Web Visits']
responders, non_responders = [5.07, 5.29], [3.91, 5.32]
x = np.arange(len(metrics))
width = 0.32
rects1 = ax.bar(x - width/2, responders, width, label='Responders (1)', color='#1a365d', zorder=3)
rects2 = ax.bar(x + width/2, non_responders, width, label='Non-Responders (0)', color='#63b3ed', zorder=3)
ax.set_title('Digital Behavior: Responders vs Non-Responders', fontsize=18, fontweight='bold', pad=25, color='#0f172a')
ax.grid(axis='y', linestyle='--', alpha=0.35, color='#94a3b8', zorder=0)
for spine in ['top', 'right', 'left']:
    ax.spines[spine].set_visible(False)
ax.spines['bottom'].set_color('#cbd5e1')
ax.spines['bottom'].set_linewidth(1.5)
ax.set_xticks(x)
ax.set_xticklabels(metrics, fontweight='bold', fontsize=13, color='#1e293b')
ax.tick_params(axis='x', pad=10)
ax.tick_params(axis='y', labelsize=11, colors='#64748b')
for bar in rects1 + rects2:
    yval = bar.get_height()
ax.text(bar.get_x() + bar.get_width()/2, yval + 0.12, f'{yval:.2f}', ha='center', va='bottom', fontweight='bold', fontsize=13, color='#0f172a')
ax.set_ylim(0, 6.8)
ax.legend(frameon=True, facecolor='#ffffff', edgecolor='#cbd5e1', fontsize=11, loc='upper center', bbox_to_anchor=(0.5, 1.02), ncol=2)
plt.tight_layout()
plt.savefig('visualizations/digital_behavior.png', bbox_inches='tight', dpi=600)
plt.close()

print("Charts created successfully!")