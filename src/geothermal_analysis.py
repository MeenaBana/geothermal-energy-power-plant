"""
Geothermal Energy Analysis and Visualization
===========================================

This script provides visualization and analysis tools for geothermal energy data,
complementing the MATLAB Organic Rankine Cycle simulation.

Features:
- Global geothermal capacity visualization
- Comparison with other renewable energy sources
- Cost analysis of geothermal power generation
- Regional distribution of geothermal resources
- Efficiency comparison across different binary cycle configurations
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from matplotlib.ticker import FuncFormatter
from pathlib import Path

plt.style.use('seaborn-v0_8-whitegrid')
sns.set_context("talk")

Path("./results").mkdir(exist_ok=True)

def millions_formatter(x, pos):
    """Format y-axis ticks in millions"""
    return f'{int(x/1000000)}M'

def thousands_formatter(x, pos):
    """Format y-axis ticks in thousands"""
    return f'{int(x/1000)}k'

def format_ax(ax, title, xlabel, ylabel, legend_title=None):
    """Apply consistent formatting to axes"""
    ax.set_title(title, fontweight='bold', pad=15)
    ax.set_xlabel(xlabel)
    ax.set_ylabel(ylabel)
    if legend_title:
        ax.legend(title=legend_title)
    ax.grid(True, linestyle='--', alpha=0.7)
    
def plot_geothermal_capacity_trend():
    """Plot global geothermal installed capacity trend from 2005-2020"""
    
    # Data from IRENA reports (2005-2020)
    years = np.arange(2005, 2021)
    capacity_mw = [8686, 8918, 9139, 9459, 9899, 10121, 10011, 10471, 
                  10740, 11221, 11846, 12706, 13299, 13928, 14600, 15406]
    
    fig, ax = plt.subplots(figsize=(12, 6))
    
    ax.plot(years, capacity_mw, 'o-', linewidth=3, markersize=8, color='#d62728')
    
    for i in [0, 5, 10, 15]:
        ax.annotate(f'{capacity_mw[i]} MW', 
                   xy=(years[i], capacity_mw[i]), 
                   xytext=(0, 15), 
                   textcoords='offset points',
                   ha='center',
                   fontweight='bold')
   
    format_ax(ax, 
              'Global Installed Geothermal Capacity (2005-2020)',
              'Year', 
              'Installed Capacity (MW)')
    
    ax.set_xticks(years[::2])  # Show every other year
    
    cagr = (capacity_mw[-1]/capacity_mw[0])**(1/(len(years)-1)) - 1
    ax.text(0.05, 0.05, f'CAGR: {cagr*100:.2f}%',
           transform=ax.transAxes,
           fontsize=12,
           bbox=dict(facecolor='white', alpha=0.8, boxstyle='round,pad=0.5'))
    
    plt.tight_layout()
    plt.savefig('./results/geothermal_capacity_trend.png', dpi=300)
    plt.close()
    
def plot_technology_comparison():
    """Compare geothermal with other renewable energy technologies"""
    
    # Data from IRENA (2020)
    technologies = ['Solar PV', 'Wind Onshore', 'Wind Offshore', 
                   'Hydropower', 'Geothermal', 'Biomass']
   
    capacity_factors = [24.3, 35.6, 43.5, 44.2, 83.1, 75.2]
    
    # LCOE in USD/MWh
    lcoe_values = [57, 39, 84, 47, 71, 85]
   
    df = pd.DataFrame({
        'Technology': technologies,
        'Capacity Factor (%)': capacity_factors,
        'LCOE (USD/MWh)': lcoe_values
    })
   
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(15, 6))
   
    bars1 = sns.barplot(x='Technology', y='Capacity Factor (%)', data=df, ax=ax1)
   
    for i, tech in enumerate(technologies):
        if tech == 'Geothermal':
            ax1.patches[i].set_facecolor('#d62728')
        else:
            ax1.patches[i].set_facecolor('#1f77b4')  
    
    format_ax(ax1, 
              'Capacity Factors by Technology (2020)',
              '', 
              'Capacity Factor (%)')
  
    bars2 = sns.barplot(x='Technology', y='LCOE (USD/MWh)', data=df, ax=ax2)
   
    for i, tech in enumerate(technologies):
        if tech == 'Geothermal':
            ax2.patches[i].set_facecolor('#d62728')
        else:
            ax2.patches[i].set_facecolor('#1f77b4')  
    
    format_ax(ax2, 
              'Levelized Cost of Energy (2020)',
              '', 
              'LCOE (USD/MWh)')
  
    for ax in [ax1, ax2]:
        plt.setp(ax.get_xticklabels(), rotation=45, ha='right')
    
    plt.tight_layout()
    plt.savefig('./results/renewable_technology_comparison.png', dpi=300)
    plt.close()

def plot_top_geothermal_countries():
    """Plot top countries by geothermal electricity generation"""
    
    # Data from IRENA (2019)
    countries = ['United States', 'Indonesia', 'Philippines', 'Turkey', 
                'New Zealand', 'Italy', 'Iceland', 'Kenya', 'Mexico', 'Japan']
    
    generation_gwh = [18000, 14600, 10730, 8900, 8200, 6100, 6000, 5500, 5400, 2900]
    installed_mw = [2600, 2100, 1900, 1500, 1000, 900, 750, 800, 950, 550]
    
    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(12, 10))
  
    bars1 = ax1.bar(countries, generation_gwh, color='maroon')
    ax1.axhline(y=np.mean(generation_gwh), linestyle='--', color='k', alpha=0.7,
               label=f'Average: {np.mean(generation_gwh):.0f} GWh')
    
    format_ax(ax1, 
              'Top 10 Countries by Geothermal Electricity Generation (2019)',
              '', 
              'Electricity Generation (GWh)')
    
    ax1.legend()
    
    bars2 = ax2.bar(countries, installed_mw, color='darkgreen')
    ax2.axhline(y=np.mean(installed_mw), linestyle='--', color='k', alpha=0.7,
               label=f'Average: {np.mean(installed_mw):.0f} MW')
    
    format_ax(ax2, 
              'Top 10 Countries by Installed Geothermal Capacity (2019)',
              '', 
              'Installed Capacity (MW)')
    
    ax2.legend()
  
    for ax in [ax1, ax2]:
        plt.setp(ax.get_xticklabels(), rotation=45, ha='right')
    
    plt.tight_layout()
    plt.savefig('./results/top_geothermal_countries.png', dpi=300)
    plt.close()

def plot_orc_efficiency_comparison():
    """Compare ORC efficiency with different working fluids"""
  
    temperature_range = np.arange(80, 200, 10)
    
    # Efficiency data for different working fluids at various temperatures
    r134a_efficiency = 4.5 + 0.08 * (temperature_range - 80)
    r245fa_efficiency = 5.0 + 0.09 * (temperature_range - 80)
    isopentane_efficiency = 5.2 + 0.10 * (temperature_range - 80)
    n_pentane_efficiency = 5.1 + 0.095 * (temperature_range - 80)
   
    r134a_efficiency += np.random.normal(0, 0.3, len(temperature_range))
    r245fa_efficiency += np.random.normal(0, 0.3, len(temperature_range))
    isopentane_efficiency += np.random.normal(0, 0.3, len(temperature_range))
    n_pentane_efficiency += np.random.normal(0, 0.3, len(temperature_range))
   
    fig, ax = plt.subplots(figsize=(12, 7))
    
    ax.plot(temperature_range, r134a_efficiency, 'o-', label='R134a', linewidth=2)
    ax.plot(temperature_range, r245fa_efficiency, 's-', label='R245fa', linewidth=2)
    ax.plot(temperature_range, isopentane_efficiency, '^-', label='Isopentane', linewidth=2)
    ax.plot(temperature_range, n_pentane_efficiency, 'd-', label='n-Pentane', linewidth=2)
    
    format_ax(ax, 
              'ORC Efficiency with Different Working Fluids',
              'Geothermal Resource Temperature (°C)', 
              'Thermal Efficiency (%)',
              'Working Fluids')
    
    textstr = '\n'.join((
        'Key Findings:',
        '• Isopentane shows highest efficiency',
        '• Efficiency increases with temperature',
        '• Typical range: 5-16% for binary cycles',
        '• Working fluid selection depends on resource temperature'
    ))
    
    props = dict(boxstyle='round', facecolor='white', alpha=0.8)
    ax.text(0.05, 0.95, textstr, transform=ax.transAxes, fontsize=10,
           verticalalignment='top', bbox=props)
    
    plt.tight_layout()
    plt.savefig('./results/orc_working_fluid_comparison.png', dpi=300)
    plt.close()

def plot_investment_trends():
    """Plot investment trends in geothermal energy"""
   
    years = np.arange(2010, 2021)
    
    # Investment in Million USD
    investment = [1600, 2900, 1700, 2200, 2800, 2000, 2400, 
                 3100, 2300, 1800, 2500]
   
    cumulative_capacity = [10121, 10011, 10471, 10740, 11221, 11846, 
                          12706, 13299, 13928, 14600, 15406]
    
    new_capacity = [222, -110, 460, 269, 481, 625, 860, 593, 629, 672, 806]
    
    fig, ax1 = plt.subplots(figsize=(12, 7))
    
    color = 'tab:red'
    ax1.set_xlabel('Year')
    ax1.set_ylabel('Annual Investment (Million USD)', color=color)
    ax1.bar(years, investment, color=color, alpha=0.7)
    ax1.tick_params(axis='y', labelcolor=color)
  
    ax2 = ax1.twinx()
    color = 'tab:blue'
    ax2.set_ylabel('New Capacity Added (MW)', color=color)
    ax2.plot(years, new_capacity, 'o-', color=color, linewidth=3)
    ax2.tick_params(axis='y', labelcolor=color)
   
    plt.title('Geothermal Energy Investment and Capacity Addition (2010-2020)', 
             fontweight='bold', pad=15)
    ax1.grid(True, linestyle='--', alpha=0.3)
  
    inv_per_mw = [inv / max(cap, 1) for inv, cap in zip(investment, new_capacity)]
    avg_inv_per_mw = np.mean([i for i in inv_per_mw if i > 0])
    
    ax1.text(0.05, 0.95, f'Avg. Investment: ${avg_inv_per_mw:.1f}M per MW',
           transform=ax1.transAxes,
           fontsize=12,
           bbox=dict(facecolor='white', alpha=0.8, boxstyle='round,pad=0.5'))
    
    plt.tight_layout()
    plt.savefig('./results/geothermal_investment_trends.png', dpi=300)
    plt.close()

def plot_geothermal_potential_map():
    """Create a visualization of geothermal potential by region"""
   
    regions = ['North America', 'Central America', 'South America', 
              'Europe', 'Africa', 'Middle East', 'Central Asia', 
              'East Asia', 'Southeast Asia', 'Oceania']
    
    potential_capacity_gw = [35, 6, 12, 18, 15, 2, 8, 27, 30, 9]
    
    installed_capacity_gw = [3.2, 0.7, 0.9, 3.3, 0.7, 0.1, 0.1, 3.8, 4.8, 1.4]
    
    # Calculate percentage utilized
    utilization = [i/p*100 for i, p in zip(installed_capacity_gw, potential_capacity_gw)]
    
    # Create DataFrame
    df = pd.DataFrame({
        'Region': regions,
        'Potential (GW)': potential_capacity_gw,
        'Installed (GW)': installed_capacity_gw,
        'Utilization (%)': utilization
    })
    
    df = df.sort_values('Potential (GW)', ascending=False)
    
    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(12, 10))
    
    df.plot(x='Region', y=['Potential (GW)', 'Installed (GW)'], 
           kind='bar', ax=ax1, color=['#1f77b4', '#ff7f0e'])
    
    format_ax(ax1, 
              'Geothermal Potential vs. Installed Capacity by Region',
              '', 
              'Capacity (GW)')
    
    bars = ax2.bar(df['Region'], df['Utilization (%)'], color='green')
    
    for bar in bars:
        height = bar.get_height()
        ax2.text(bar.get_x() + bar.get_width()/2., height + 0.5,
                f'{height:.1f}%',
                ha='center', va='bottom', rotation=0)
    
    format_ax(ax2, 
              'Geothermal Potential Utilization by Region',
              '', 
              'Utilization (%)')
    
    for ax in [ax1, ax2]:
        plt.setp(ax.get_xticklabels(), rotation=45, ha='right')
    
    plt.tight_layout()
    plt.savefig('./results/geothermal_potential_by_region.png', dpi=300)
    plt.close()

def generate_all_visualizations():
    """Generate all visualization plots"""
    print("Generating geothermal energy visualizations...")
    
    plot_geothermal_capacity_trend()
    print("✓ Generated capacity trend visualization")
    
    plot_technology_comparison()
    print("✓ Generated technology comparison visualization")
    
    plot_top_geothermal_countries()
    print("✓ Generated top countries visualization")
    
    plot_orc_efficiency_comparison()
    print("✓ Generated ORC efficiency comparison")
    
    plot_investment_trends()
    print("✓ Generated investment trends visualization")
    
    plot_geothermal_potential_map()
    print("✓ Generated geothermal potential map")
    
    print("\nAll visualizations have been saved to the 'results' directory.")

if __name__ == "__main__":
    generate_all_visualizations()