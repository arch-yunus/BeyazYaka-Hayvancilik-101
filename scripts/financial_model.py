#!/usr/bin/env python3
"""
financial_model.py — THE LIVESTOCK ENCYCLOPEDIA: Finansal Model
ROI, Break-even, Nakit Akışı ve 5 Yıllık Projeksiyon
"""

from dataclasses import dataclass, field
from typing import List

@dataclass
class FarmParameters:
    # Sürü
    herd_size: int = 50                     # Laktasyondaki inek sayısı
    daily_milk_per_cow: float = 28.0        # L/gün
    lactation_days: int = 305               # Yıllık laktasyon gün sayısı
    culling_rate: float = 0.25              # Yıllık sürü çıkış oranı

    # Klinik Gelirler
    milk_price_per_liter: float = 20.0      # TL/L
    calf_sale_price: float = 15000.0        # TL/buzağı
    culled_cow_price: float = 50000.0       # TL/baş
    manure_revenue_per_year: float = 30000.0  # TL

    # Yem
    daily_feed_cost_per_cow: float = 350.0  # TL/gün/baş

    # Sabit Giderler (Aylık)
    labor_cost_monthly: float = 70000.0
    vet_monthly: float = 25000.0
    insemination_monthly: float = 10000.0
    utilities_monthly: float = 30000.0
    depreciation_monthly: float = 40000.0
    other_monthly: float = 15000.0

    # Yatırım
    total_investment: float = 10_900_000.0

@dataclass
class YearlyResults:
    year: int
    herd_size: int
    revenue: float
    feed_cost: float
    fixed_cost: float
    net_profit: float
    cumulative_cash_flow: float

def run_financial_model(params: FarmParameters, years: int = 5) -> List[YearlyResults]:
    results = []
    cumulative_cf = -params.total_investment

    current_herd = params.herd_size

    for y in range(1, years + 1):
        # Gelirler
        milk_revenue = (current_herd * params.daily_milk_per_cow *
                        params.lactation_days * params.milk_price_per_liter)
        calf_revenue = current_herd * 0.85 * params.calf_sale_price   # %85 buzağı hayatta kalır
        culled_revenue = current_herd * params.culling_rate * params.culled_cow_price
        total_revenue = milk_revenue + calf_revenue + culled_revenue + params.manure_revenue_per_year

        # Değişken Gider (Yem)
        feed_cost = current_herd * params.daily_feed_cost_per_cow * 365.0

        # Sabit Gider
        fixed_monthly_total = (params.labor_cost_monthly + params.vet_monthly +
                               params.insemination_monthly + params.utilities_monthly +
                               params.depreciation_monthly + params.other_monthly)
        fixed_annual = fixed_monthly_total * 12

        # Kar
        total_cost = feed_cost + fixed_annual
        net_profit = total_revenue - total_cost
        cumulative_cf += net_profit

        results.append(YearlyResults(
            year=y,
            herd_size=current_herd,
            revenue=total_revenue,
            feed_cost=feed_cost,
            fixed_cost=fixed_annual,
            net_profit=net_profit,
            cumulative_cash_flow=cumulative_cf
        ))

        # Sürü büyümesi (%15 her yıl, eğer karlıysa)
        if net_profit > 0:
            current_herd = int(current_herd * 1.15)

    return results

def print_report(params: FarmParameters, results: List[YearlyResults]):
    print("\n" + "=" * 70)
    print("  THE LIVESTOCK ENCYCLOPEDIA - 5 YILLIK FİNANSAL PROJEKSİYON")
    print("=" * 70)
    print(f"  Başlangıç Sürü: {params.herd_size} baş | Başlangıç Yatırımı: {params.total_investment:,.0f} TL")
    print(f"  Günlük Süt: {params.daily_milk_per_cow}L/baş | Süt Fiyatı: {params.milk_price_per_liter} TL/L")
    print("-" * 70)
    print(f"{'Yıl':>4} | {'Sürü':>6} | {'Gelir (TL)':>14} | {'Gider (TL)':>14} | {'Net Kar (TL)':>14} | {'Kümülatif CF':>14}")
    print("-" * 70)

    breakeven_year = None
    for r in results:
        total_cost = r.feed_cost + r.fixed_cost
        marker = " <-- BREAK-EVEN" if r.cumulative_cash_flow >= 0 and breakeven_year is None else ""
        if marker:
            breakeven_year = r.year
        print(f"{r.year:>4} | {r.herd_size:>6} | {r.revenue:>14,.0f} | {total_cost:>14,.0f} | {r.net_profit:>14,.0f} | {r.cumulative_cash_flow:>14,.0f}{marker}")

    print("=" * 70)

    if breakeven_year:
        print(f"\n  [OK] Break-even Point: {breakeven_year}. YIL")
    else:
        print(f"\n  [!!] 5 Yilda Break-even saglanamadi. Parametreleri gozden gecirin.")

    print()

    # Sut Yem Paritesi
    feed_per_kg = (params.daily_feed_cost_per_cow / (params.daily_milk_per_cow))
    parity = params.milk_price_per_liter / (params.daily_feed_cost_per_cow / params.daily_milk_per_cow)
    print(f"  [KPI] Sut-Yem Paritesi: {parity:.2f}  (>1.5 -> Karli, <1.0 -> Kriz)")

if __name__ == "__main__":
    params = FarmParameters(
        herd_size=50,
        daily_milk_per_cow=30.0,
        milk_price_per_liter=20.0,
        daily_feed_cost_per_cow=380.0,
        total_investment=10_900_000.0
    )
    results = run_financial_model(params, years=5)
    print_report(params, results)
