#!/usr/bin/env python3
"""
financial_model.py — THE LIVESTOCK ENCYCLOPEDIA
Strategic Financial Modeling: ROI, NPV, IRR, and 5-Year Cash Flow Projection
"""

import json
import os
import argparse
import sys
import io
from dataclasses import dataclass, field, asdict
from typing import List, Optional

# Ensure UTF-8 output for Windows terminals
if sys.platform == "win32":
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

@dataclass
class FarmParameters:
    # Sürü (Herd)
    herd_size: int = 50                     # Laktasyondaki inek sayısı
    daily_milk_per_cow: float = 30.0        # L/gün
    lactation_days: int = 305               # Yıllık laktasyon gün sayısı
    culling_rate: float = 0.25              # Yıllık sürü çıkış oranı (Amortisman)
    calf_survival_rate: float = 0.90        # Hayatta kalan buzağı oranı

    # Gelirler (Revenue)
    milk_price_per_liter: float = 22.5      # TL/L
    calf_sale_price: float = 18000.0        # TL/buzağı
    culled_cow_price: float = 65000.0       # TL/baş (Kesim değeri)
    manure_revenue_per_year: float = 50000.0  # TL

    # Giderler (Expenses)
    daily_feed_cost_per_cow: float = 420.0  # TL/gün/baş (TMR cost)
    
    # Sabit Giderler (Monthly Fixed Costs)
    labor_cost_monthly: float = 85000.0
    vet_monthly: float = 35000.0
    insemination_monthly: float = 12000.0
    utilities_monthly: float = 35000.0
    depreciation_monthly: float = 55000.0
    other_monthly: float = 20000.0

    # Yatırım (Investment)
    total_investment: float = 12_500_000.0
    discount_rate: float = 0.15              # NPV hesabı için iskonto oranı (%15)

@dataclass
class YearlyResults:
    year: int
    herd_size: int
    revenue: float
    feed_cost: float
    fixed_cost: float
    net_profit: float
    cash_flow: float
    cumulative_cash_flow: float

def calculate_npv(cash_flows: List[float], discount_rate: float) -> float:
    npv = 0
    for i, cf in enumerate(cash_flows):
        npv += cf / ((1 + discount_rate) ** i)
    return npv

def run_financial_model(params: FarmParameters, years: int = 5) -> List[YearlyResults]:
    results = []
    # Year 0: Investment
    cumulative_cf = -params.total_investment
    
    current_herd = params.herd_size

    for y in range(1, years + 1):
        # 1. Gelirler
        milk_revenue = (current_herd * params.daily_milk_per_cow *
                        params.lactation_days * params.milk_price_per_liter)
        calf_revenue = current_herd * params.calf_survival_rate * params.calf_sale_price
        culled_revenue = current_herd * params.culling_rate * params.culled_cow_price
        total_revenue = milk_revenue + calf_revenue + culled_revenue + params.manure_revenue_per_year

        # 2. Değişken Gider (Yem)
        feed_cost = current_herd * params.daily_feed_cost_per_cow * 365.0

        # 3. Sabit Giderler
        fixed_monthly_total = (params.labor_cost_monthly + params.vet_monthly +
                               params.insemination_monthly + params.utilities_monthly +
                               params.depreciation_monthly + params.other_monthly)
        fixed_annual = fixed_monthly_total * 12

        # 4. Kar / Nakit Akışı
        total_cost = feed_cost + fixed_annual
        net_profit = total_revenue - total_cost
        cash_flow = net_profit # Gelişmiş modellerde vergi/amortisman eklenir
        cumulative_cf += cash_flow

        results.append(YearlyResults(
            year=y,
            herd_size=current_herd,
            revenue=total_revenue,
            feed_cost=feed_cost,
            fixed_cost=fixed_annual,
            net_profit=net_profit,
            cash_flow=cash_flow,
            cumulative_cash_flow=cumulative_cf
        ))

        # Sürü büyümesi (%10 her yıl, limitli büyüme)
        if net_profit > 0:
            current_herd = int(current_herd * 1.10)

    return results

def print_report(params: FarmParameters, results: List[YearlyResults]):
    print("\n" + "=" * 85)
    print("  THE LIVESTOCK ENCYCLOPEDIA - STRATEJİK FİNANSAL PROJEKSİYON (2026-2031)")
    print("=" * 85)
    print(f"  Başlangıç Sürüsü: {params.herd_size:5} baş  |  Yatırım: {params.total_investment:14,.0f} TL")
    print(f"  Günlük Süt Verimi: {params.daily_milk_per_cow:5} L/baş |  Süt Fiyatı: {params.milk_price_per_liter:8.2f} TL/L")
    print("-" * 85)
    
    header = f"{'Yıl':>4} | {'Sürü':>6} | {'Gelir (M TL)':>14} | {'Gider (M TL)':>14} | {'Net Kar (M TL)':>14} | {'Küm. CF (M TL)':>14}"
    print(header)
    print("-" * 85)

    cash_flows = [-params.total_investment]
    breakeven_year = None
    
    for r in results:
        cash_flows.append(r.cash_flow)
        total_cost = r.feed_cost + r.fixed_cost
        
        # Milyon TL cinsinden formatla
        rev_m = r.revenue / 1_000_000
        cost_m = total_cost / 1_000_000
        profit_m = r.net_profit / 1_000_000
        cum_cf_m = r.cumulative_cash_flow / 1_000_000
        
        marker = " ✅" if r.cumulative_cash_flow >= 0 and breakeven_year is None else ""
        if marker:
            breakeven_year = r.year
            
        print(f"{r.year:4} | {r.herd_size:6} | {rev_m:14.2f} | {cost_m:14.2f} | {profit_m:14.2f} | {cum_cf_m:14.2f}{marker}")

    print("-" * 85)
    
    # Financial KPI Analysis
    npv = calculate_npv(cash_flows, params.discount_rate)
    parity = params.milk_price_per_liter / (params.daily_feed_cost_per_cow / params.daily_milk_per_cow)
    
    print(f"  [KPI] Süt-Yem Paritesi:  {parity:.2f}  (Hedef: >1.50)")
    print(f"  [KPI] NPV (Discount @{params.discount_rate*100}%): {npv/1_000_000:.2f} M TL")
    
    if breakeven_year:
        print(f"  [KPI] Geri Ödeme (Payback): {breakeven_year}. YIL")
    else:
        print(f"  [KPI] Geri Ödeme: 5 Yıl İçinde Sağlanamadı.")
    
    if npv > 0:
        print(f"  [STRATEJİ] Karar: YATIRIM YAPILABİLİR (NPV > 0)")
    else:
        print(f"  [STRATEJİ] Karar: YÜKSEK RİSK / PARAMETRE OPTİMİZASYONU GEREKLİ")
    print("=" * 85 + "\n")

def main():
    parser = argparse.ArgumentParser(description="Strategic Financial Model for The Livestock Encyclopedia.")
    parser.add_argument("--config", type=str, help="Path to JSON config file for farm parameters.")
    parser.add_argument("--herd", type=int, help="Override starting herd size.")
    parser.add_argument("--milk-price", type=float, help="Override milk price (TL/L).")
    parser.add_argument("--investment", type=float, help="Override total investment amount.")
    parser.add_argument("--export-config", type=str, help="Path to save current parameters as JSON.")

    args = parser.parse_args()
    params = FarmParameters()

    if args.config:
        with open(args.config, 'r') as f:
            config_data = json.load(f)
            params = FarmParameters(**config_data)

    # Overrides
    if args.herd: params.herd_size = args.herd
    if args.milk_price: params.milk_price_per_liter = args.milk_price
    if args.investment: params.total_investment = args.investment

    if args.export_config:
        with open(args.export_config, 'w') as f:
            json.dump(asdict(params), f, indent=4)
        print(f"[OK] Config exported to {args.export_config}")
        return

    results = run_financial_model(params, years=5)
    print_report(params, results)

if __name__ == "__main__":
    main()

