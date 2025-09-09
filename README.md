# Numerical Calculus Projects – 2024  

This repository contains computational projects developed in 2024 for the **Numerical Calculus (MS211)** course at the University of Campinas (Unicamp). The projects combine theoretical concepts from numerical analysis with practical implementations in Python.  

## 📂 Repository Structure  

- **`cholesky.py`** → Code for **Project I** (Cholesky Factorization).  
- **`projetoII_calcnum.py`** → Code for **Project II** (ODE Solvers and Population Growth Modeling).  
- **`PCI_247844_281199.pdf`** → Report for Project I.  
- **`PCII_247844_281199.pdf`** → Report for Project II.  

---

## 📘 Project I – Cholesky Factorization  

**Goal:**  
Implement and analyze the **Cholesky decomposition**, which factorizes a symmetric and positive-definite matrix into the product of a lower triangular matrix and its transpose.  

**Highlights:**  
- Verification of matrix symmetry and positive-definiteness.  
- Step-by-step implementation of the decomposition algorithm.  
- Error handling for non-positive-definite matrices.  
- Comparison with analytical results.  

**Usage:**  
The script `cholesky.py` demonstrates the factorization process using example matrices.  

---

## 📘 Project II – ODE Solvers and Population Growth  

**Goal:**  
Apply numerical methods to solve **initial value problems (IVPs)** and model **population growth dynamics**.  

**Part I – IVPs:**  
- Implementation of **Improved Euler** and **Runge-Kutta 4th Order (RK4)** methods.  
- Comparison of numerical approximations with the analytical solution.  
- Visualization of results with **Matplotlib**.  

**Part II – Population Growth:**  
- Modeling population growth using the **logistic differential equation**.  
- Solution obtained with **`scipy.integrate.odeint`**.  
- Comparison with the exact analytical solution.  
- Export of results to an **Excel table** with computed errors.  

**Usage:**  
Run `projetoII_calcnum.py` to:  
- Generate and plot the numerical vs analytical solutions for the IVP.  
- Compute population growth with `odeint` and export results to Excel.  

---

## 🛠️ Requirements  

Both projects require **Python 3** and the following libraries:  

```bash
pip install numpy matplotlib pandas scipy
```

---

## 🚀 How to Run

1. Clone the repository:
```bash
git clone https://github.com/gabrielantunes7/MS211_2024.git
cd MS211_2024
```

2. Run Project I (Cholesky Factorization):
```bash
python projeto01/projetoI_calcnum.py
```

3. Run Project II (ODE Solvers & Population Growth):
```bash
python projeto02/projetoII_calcnum.py
```

---

## 📑 Authors
- Felipe Lobão Melara
- Gabriel Mattias Antunes
