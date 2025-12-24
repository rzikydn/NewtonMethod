import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.patches import FancyArrowPatch
import random

# Page configuration
st.set_page_config(
    page_title="Newton Method - Metode Numerik",
    page_icon="📐",
    layout="wide"
)

# Custom CSS
st.markdown("""
    <style>
    .main-header {
        font-size: 2.5rem;
        color: #1f77b4;
        text-align: center;
        font-weight: bold;
        margin-bottom: 1rem;
    }
    .sub-header {
        font-size: 1.2rem;
        color: #555;
        text-align: center;
        margin-bottom: 2rem;
    }
    .info-box {
        background-color: #e7f3ff;
        padding: 1rem;
        border-radius: 0.5rem;
        border-left: 5px solid #1f77b4;
        margin: 1rem 0;
        color: #1a1a1a;
        font-weight: 500;
    }
    .success-box {
        background-color: #d4edda;
        padding: 1rem;
        border-radius: 0.5rem;
        border-left: 5px solid #28a745;
        margin: 1rem 0;
        color: #155724;
        font-weight: 500;
    }
    .warning-box {
        background-color: #fff3cd;
        padding: 1rem;
        border-radius: 0.5rem;
        border-left: 5px solid #ffc107;
        margin: 1rem 0;
        color: #856404;
        font-weight: 500;
    }
    </style>
""", unsafe_allow_html=True)

# Title
st.markdown('<div class="main-header"> NEWTON METHOD</div>', unsafe_allow_html=True)
st.markdown('<div class="sub-header">Metode Numerik untuk Mencari Akar Persamaan</div>', unsafe_allow_html=True)

# Newton Method Function
def newton_method(func, func_derivative, x0, tolerance, max_iterations):
    """
    Implementasi Newton Method
    Returns: list of iterations with details
    """
    iterations = []
    xn = x0
    
    for i in range(max_iterations):
        try:
            fx = func(xn)
            fpx = func_derivative(xn)
            
            if abs(fpx) < 1e-10:
                st.error("⚠️ Turunan mendekati nol! Metode tidak dapat dilanjutkan.")
                break
            
            xn_plus_1 = xn - fx / fpx
            error = abs(xn_plus_1 - xn)
            
            status = "Konvergen" if error < tolerance else "Lanjut"
            
            iterations.append({
                'Iterasi': i,
                'xₙ': xn,
                'f(xₙ)': fx,
                "f'(xₙ)": fpx,
                'xₙ₊₁': xn_plus_1,
                '|xₙ₊₁ - xₙ|': error,
                'Status': status
            })
            
            if error < tolerance:
                break
            
            xn = xn_plus_1
            
        except Exception as e:
            st.error(f"❌ Error pada iterasi {i}: {str(e)}")
            break
    
    return iterations

# Generate random polynomial
def generate_random_polynomial():
    """Generate random polynomial function"""
    degree = random.choice([2, 3])
    
    if degree == 2:
        a = random.randint(-5, 5)
        b = random.randint(-10, 10)
        c = random.randint(-10, 10)
        
        if a == 0:
            a = random.choice([-3, -2, -1, 1, 2, 3])
        
        func_str = f"{a}x² + {b}x + {c}"
        deriv_str = f"{2*a}x + {b}"
        
        func = lambda x: a * x**2 + b * x + c
        deriv = lambda x: 2 * a * x + b
        
    else:  # degree == 3
        a = random.randint(-3, 3)
        b = random.randint(-5, 5)
        c = random.randint(-10, 10)
        d = random.randint(-10, 10)
        
        if a == 0:
            a = random.choice([-2, -1, 1, 2])
        
        func_str = f"{a}x³ + {b}x² + {c}x + {d}"
        deriv_str = f"{3*a}x² + {2*b}x + {c}"
        
        func = lambda x: a * x**3 + b * x**2 + c * x + d
        deriv = lambda x: 3 * a * x**2 + 2 * b * x + c
    
    # Clean up display
    func_str = func_str.replace("+ -", "- ").replace(" 1x", " x").replace("^", "**")
    deriv_str = deriv_str.replace("+ -", "- ").replace(" 1x", " x").replace("^", "**")
    
    return func, deriv, func_str, deriv_str

# Plot function and Newton Method steps
def plot_newton_method(func, iterations, x_range=None):
    """Plot fungsi dan visualisasi Newton Method"""
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 5))
    
    # Get x values from iterations
    x_values = [it['xₙ'] for it in iterations]
    
    # Auto-range if not provided
    if x_range is None:
        x_min = min(x_values) - 2
        x_max = max(x_values) + 2
    else:
        x_min, x_max = x_range
    
    # Plot 1: Function and convergence points
    x = np.linspace(x_min, x_max, 500)
    try:
        y = [func(xi) for xi in x]
        ax1.plot(x, y, 'b-', linewidth=2, label='f(x)')
        ax1.axhline(y=0, color='k', linestyle='--', alpha=0.3)
        ax1.grid(True, alpha=0.3)
        
        # Plot iteration points
        for i, it in enumerate(iterations):
            if i < len(iterations) - 1:
                ax1.plot(it['xₙ'], it['f(xₙ)'], 'ro', markersize=8, alpha=0.6)
                ax1.annotate(f"x{i}", (it['xₙ'], it['f(xₙ)']), 
                           textcoords="offset points", xytext=(0,10), ha='center')
        
        # Plot final point
        final = iterations[-1]
        ax1.plot(final['xₙ₊₁'], func(final['xₙ₊₁']), 'go', markersize=12, 
                label=f"Akar ≈ {final['xₙ₊₁']:.6f}")
        
        ax1.set_xlabel('x', fontsize=12)
        ax1.set_ylabel('f(x)', fontsize=12)
        ax1.set_title('Fungsi dan Titik Iterasi Newton Method', fontsize=14, fontweight='bold')
        ax1.legend()
        
    except Exception as e:
        ax1.text(0.5, 0.5, f'Error plotting function: {str(e)}', 
                ha='center', va='center', transform=ax1.transAxes)
    
    # Plot 2: Error convergence
    errors = [it['|xₙ₊₁ - xₙ|'] for it in iterations]
    iterations_num = [it['Iterasi'] for it in iterations]
    
    ax2.semilogy(iterations_num, errors, 'r-o', linewidth=2, markersize=6)
    ax2.grid(True, alpha=0.3)
    ax2.set_xlabel('Iterasi', fontsize=12)
    ax2.set_ylabel('Error |xₙ₊₁ - xₙ| (log scale)', fontsize=12)
    ax2.set_title('Konvergensi Error', fontsize=14, fontweight='bold')
    
    plt.tight_layout()
    return fig

# Sidebar for mode selection
st.sidebar.title("SIDE BAR")
mode = st.sidebar.radio(
    "Pilih Mode:",
    ["🎲 Random Mode", "✍️ Manual Input Mode"],
    help="Random Mode: Generate fungsi random\nManual Mode: Input fungsi sendiri"
)

st.sidebar.markdown("---")
st.sidebar.markdown("###  TENTANG NEWTON METHOD")
st.sidebar.info("""
**Formula:**
xₙ₊₁ = xₙ - f(xₙ)/f'(xₙ)

**Kondisi Berhenti:**
- |xₙ₊₁ - xₙ| < toleransi
- Iterasi maksimum tercapai
""")

# Main Content
if mode == "🎲 Random Mode":
    st.markdown("##  MODE : RANDOM FUNCTION GENERATOR")
    st.markdown('<div class="info-box">Mode ini akan generate fungsi polynomial secara random dan otomatis menghitung akarnya menggunakan Newton Method.</div>', unsafe_allow_html=True)

    if st.button("🎲 Generate Random Function", type="primary", use_container_width=True):
        func, deriv, func_str, deriv_str = generate_random_polynomial()

        st.session_state['random_func'] = func
        st.session_state['random_deriv'] = deriv
        st.session_state['random_func_str'] = func_str
        st.session_state['random_deriv_str'] = deriv_str

    st.markdown("###  PARAMETER")
    col1, col2, col3 = st.columns(3)

    with col1:
        x0_random = st.number_input("Tebakan Awal (x₀)", value=2.0, step=0.1, key="x0_random")
    with col2:
        tolerance_random = st.number_input("Toleransi", value=0.0001, format="%.6f", key="tol_random")
    with col3:
        max_iter_random = st.number_input("Max Iterasi", value=20, min_value=1, max_value=100, key="max_random")
    
    if 'random_func' in st.session_state:
        st.markdown("---")
        st.markdown("###  FUNGSI YANG DI GENERATE :")
        
        col_func, col_deriv = st.columns(2)
        with col_func:
            st.markdown(f'<div class="info-box"><b>f(x) = {st.session_state["random_func_str"]}</b></div>', unsafe_allow_html=True)
        with col_deriv:
            st.markdown(f'<div class="info-box"><b>f\'(x) = {st.session_state["random_deriv_str"]}</b></div>', unsafe_allow_html=True)
        
        if st.button("🚀 Hitung dengan Newton Method", type="primary", use_container_width=True):
            with st.spinner("Menghitung..."):
                iterations = newton_method(
                    st.session_state['random_func'],
                    st.session_state['random_deriv'],
                    x0_random,
                    tolerance_random,
                    max_iter_random
                )
                
                if iterations:
                    st.session_state['random_iterations'] = iterations
        
        if 'random_iterations' in st.session_state:
            iterations = st.session_state['random_iterations']
            
            # Results Summary
            final = iterations[-1]
            st.markdown("---")
            st.markdown("##  HASIL PERHITUNGAN")
            
            col1, col2, col3 = st.columns(3)
            with col1:
                st.metric("Akar Persamaan (x)", f"{final['xₙ₊₁']:.8f}")
            with col2:
                st.metric("f(x)", f"{final['f(xₙ)']:.8f}")
            with col3:
                st.metric("Jumlah Iterasi", len(iterations))
            
            # Iteration Table
            st.markdown("###  TABEL ITERASI")
            df = pd.DataFrame(iterations)
            st.dataframe(df.style.format({
                'xₙ': '{:.8f}',
                'f(xₙ)': '{:.8f}',
                "f'(xₙ)": '{:.8f}',
                'xₙ₊₁': '{:.8f}',
                '|xₙ₊₁ - xₙ|': '{:.8f}'
            }), use_container_width=True)
            
            # Visualization
            st.markdown("###  VISUALISASI")
            fig = plot_newton_method(st.session_state['random_func'], iterations)
            st.pyplot(fig)
            
            # Download CSV
            csv = df.to_csv(index=False)
            st.download_button(
                label=" DOWNLOAD HASIL (CSV)",
                data=csv,
                file_name="newton_method_random_results.csv",
                mime="text/csv",
            )

elif mode == "✍️ Manual Input Mode":
    st.markdown("##  MODE : MANUAL INPUT")
    st.markdown('<div class="info-box">Masukkan fungsi dan turunannya secara manual untuk dihitung menggunakan Newton Method.</div>', unsafe_allow_html=True)

    st.markdown('<div class="warning-box"><b> FORMAT PENULISAN:</b><br>• Gunakan <code>x</code> sebagai variabel<br>• Pangkat: <code>x**2</code>, <code>x**3</code><br>• Perkalian: <code>2*x</code>, <code>3*x**2</code><br>• Contoh: <code>x**3 - x - 2</code></div>', unsafe_allow_html=True)

    st.markdown("###  INPUT FUNGSI")

    func_input = st.text_input(
        "Fungsi f(x):",
        value="x**3 - x - 2",
        help="Contoh: x**3 - x - 2, x**2 + 3*x + 2, x**2 - 4"
    )

    deriv_input = st.text_input(
        "Turunan f'(x):",
        value="3*x**2 - 1",
        help="Contoh: 3*x**2 - 1, 2*x + 3, 2*x"
    )

    st.markdown("###  PARAMETER")
    col1, col2, col3, col4, col5 = st.columns(5)

    with col1:
        x0_manual = st.number_input("Tebakan Awal (x₀)", value=2.0, step=0.1, key="x0_manual")
    with col2:
        tolerance_manual = st.number_input("Toleransi", value=0.0001, format="%.6f", key="tol_manual")
    with col3:
        max_iter_manual = st.number_input("Max Iterasi", value=20, min_value=1, max_value=100, key="max_manual")
    with col4:
        x_min = st.number_input("Plot Range Min", value=-5.0, key="xmin")
    with col5:
        x_max = st.number_input("Plot Range Max", value=5.0, key="xmax")
    
    st.markdown("---")
    
    if st.button("🚀 Hitung dengan Newton Method", type="primary", use_container_width=True):
        try:
            # Create functions from input strings
            func = lambda x: eval(func_input)
            deriv = lambda x: eval(deriv_input)
            
            # Test if functions work
            test_val = func(1.0)
            test_deriv = deriv(1.0)
            
            with st.spinner("Menghitung..."):
                iterations = newton_method(func, deriv, x0_manual, tolerance_manual, max_iter_manual)
                
                if iterations:
                    # Results Summary
                    final = iterations[-1]
                    st.markdown("##  HASIL PERHITUNGAN")
                    
                    if final['Status'] == 'Konvergen':
                        st.markdown(f'<div class="success-box"><h3> KONVERGEN!</h3>Akar persamaan ditemukan setelah <b>{len(iterations)}</b> iterasi</div>', unsafe_allow_html=True)
                    else:
                        st.markdown(f'<div class="warning-box"><h3> BELUM KONEVERGEN</h3>Mencapai iterasi maksimum ({max_iter_manual})</div>', unsafe_allow_html=True)
                    
                    col1, col2, col3 = st.columns(3)
                    with col1:
                        st.metric("Akar Persamaan (x)", f"{final['xₙ₊₁']:.8f}")
                    with col2:
                        st.metric("f(x)", f"{final['f(xₙ)']:.8f}")
                    with col3:
                        st.metric("Jumlah Iterasi", len(iterations))
                    
                    # Iteration Table
                    st.markdown("###  TABEL ITERASI LENGKAP")
                    df = pd.DataFrame(iterations)
                    st.dataframe(df.style.format({
                        'xₙ': '{:.8f}',
                        'f(xₙ)': '{:.8f}',
                        "f'(xₙ)": '{:.8f}',
                        'xₙ₊₁': '{:.8f}',
                        '|xₙ₊₁ - xₙ|': '{:.8f}'
                    }), use_container_width=True)
                    
                    # Visualization
                    st.markdown("###  VISUALISASI")
                    fig = plot_newton_method(func, iterations, x_range=(x_min, x_max))
                    st.pyplot(fig)
                    
                    # Process Details
                    with st.expander("🔍 Lihat Detail Proses per Iterasi"):
                        for it in iterations:
                            st.markdown(f"""
                            **Iterasi {it['Iterasi']}:**
                            - xₙ = {it['xₙ']:.8f}
                            - f(xₙ) = {it['f(xₙ)']:.8f}
                            - f'(xₙ) = {it["f'(xₙ)"]:.8f}
                            - xₙ₊₁ = xₙ - f(xₙ)/f'(xₙ) = {it['xₙ']:.8f} - ({it['f(xₙ)']:.8f}/{it["f'(xₙ)"]:.8f}) = **{it['xₙ₊₁']:.8f}**
                            - Error = |{it['xₙ₊₁']:.8f} - {it['xₙ']:.8f}| = {it['|xₙ₊₁ - xₙ|']:.8f}
                            - Status: **{it['Status']}**
                            """)
                            st.markdown("---")
                    
                    # Download CSV
                    csv = df.to_csv(index=False)
                    st.download_button(
                        label="📥 Download Hasil (CSV)",
                        data=csv,
                        file_name="newton_method_manual_results.csv",
                        mime="text/csv",
                    )
                    
        except Exception as e:
            st.error(f"❌ Error: {str(e)}")
            st.markdown('<div class="warning-box">Pastikan format fungsi sudah benar. Gunakan <code>x</code> sebagai variabel dan <code>**</code> untuk pangkat.</div>', unsafe_allow_html=True)

# Footer
