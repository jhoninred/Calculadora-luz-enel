import tkinter as tk

def calcular_boleta():
    try:
        lectura_anterior = float(entry_lectura_anterior.get())
        lectura_actual = float(entry_lectura_actual.get())
        consumo = lectura_actual - lectura_anterior

        # Tarifas:
        tarifa_energia = 205.43    # CLP/kWh
        tarifa_transporte = 16.18  # CLP/kWh
        cargo_administracion = 694
        monto_exento = 198
        iva_porcentaje = 0.19

        # Cálculos
        costo_energia = consumo * tarifa_energia
        costo_transporte = consumo * tarifa_transporte
        subtotal_afecto = costo_energia + costo_transporte + cargo_administracion
        iva = subtotal_afecto * iva_porcentaje
        total_estimado = subtotal_afecto + iva + monto_exento

        resultado = (
            f"Consumo (kWh): {consumo:.1f} kWh\n"
            f"Costo energía: ${costo_energia:.0f}\n"
            f"Costo transporte: ${costo_transporte:.0f}\n"
            f"Administración: ${cargo_administracion:.0f}\n"
            f"Total: ${subtotal_afecto:.0f}\n"
        )
        etiqueta_resultado.config(text=resultado)
    except ValueError:
        etiqueta_resultado.config(text="Error: Ingresa valores numéricos válidos.")

# Interfaz
ventana = tk.Tk()
ventana.title("Calculadora Boleta Enel")
ventana.geometry("400x400")

tk.Label(ventana, text="Lectura anterior (kWh):").pack()
entry_lectura_anterior = tk.Entry(ventana)
entry_lectura_anterior.pack()

tk.Label(ventana, text="Lectura actual (kWh):").pack()
entry_lectura_actual = tk.Entry(ventana)
entry_lectura_actual.pack()

tk.Button(ventana, text="Calcular boleta", command=calcular_boleta).pack(pady=5)

etiqueta_resultado = tk.Label(ventana, text="", justify="left", font=("Courier", 10))
etiqueta_resultado.pack(pady=5)

ventana.mainloop()
