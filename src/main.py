import time
from datetime import datetime
import random
import os
import csv
from structures import List, ABR, AVL

def insert_linear_test(struttura, n):
    """
    Testa il caso peggiore inserendo 'n' elementi in ordine sequenziale (da 1 a n).
    Ritorna il tempo totale, l'array dei tempi cumulativi e i rispettivi indici (ops).
    """
    tempi_cumulativi = []
    ops = []
    step = max(1, n // 50) 
    
    tempo_iniziale = time.perf_counter()
    for i in range(1, n + 1):
        struttura.insert(i)
        if i % step == 0 or i == n:
            tempi_cumulativi.append(time.perf_counter() - tempo_iniziale)
            ops.append(i)
            
    tempo_totale = time.perf_counter() - tempo_iniziale
    return tempo_totale, tempi_cumulativi, ops


def run_all_benchmarks(num_selects, sizes):
    output_lines = []
    csv_insert_avg = [["N_Test", "Numero_Operazioni", "Lista_Time", "ABR_Time", "AVL_Time"]]
    csv_select_avg = [["N_Test", "Numero_Operazioni", "Lista_Time", "ABR_Time", "AVL_Time"]]
    csv_rank_avg   = [["N_Test", "Numero_Operazioni", "Lista_Time", "ABR_Time", "AVL_Time"]]
    csv_insert_worst = [["N_Test", "Numero_Operazioni", "Lista_Time", "ABR_Time", "AVL_Time"]]
    
    def log(message):
        print(message)
        output_lines.append(message)

    # =========================================================
    # PARTE 1: CASO MEDIO (Costruzione Casuale + Ricerche)
    # =========================================================
    log("\n" + "="*90)
    log(f"CASO MEDIO: DATI CASUALI ({num_selects} ricerche per N) - {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    log("="*90)
    log(f"{'N Elements':<12} | {'Structure':<12} | {'Insert Time':<18} | {'Select Time':<18} | {'Rank Time':<18}")
    log("-"*90)
    
    for n in sizes:
        random_data = random.sample(range(1, n * 10), n)
        search_indices = [random.randint(1, n) for _ in range(num_selects)]
        search_keys = random.choices(random_data, k=num_selects)
        step_n = max(1, n // 50)
        step_s = max(1, num_selects // 50)
        
        # --- TEST LISTA ---
        my_list = List()
        
        # Insert
        t_ins_list_g = []; ops_ins = []
        start_time = time.perf_counter()
        for i, val in enumerate(random_data, 1):
            my_list.insert(val)
            if i % step_n == 0 or i == n:
                t_ins_list_g.append(time.perf_counter() - start_time)
                ops_ins.append(i)
        t_insert_list = time.perf_counter() - start_time
        
        # Select
        t_sel_list_g = []; ops_sel = []
        start_time = time.perf_counter()
        for i, idx in enumerate(search_indices, 1):
            my_list.select(idx)
            if i % step_s == 0 or i == num_selects:
                t_sel_list_g.append(time.perf_counter() - start_time)
                ops_sel.append(i)
        t_select_list = time.perf_counter() - start_time
        
        # Rank
        t_rnk_list_g = []; ops_rnk = []
        start_time = time.perf_counter()
        for i, k in enumerate(search_keys, 1):
            my_list.rank(my_list.root, k)
            if i % step_s == 0 or i == num_selects:
                t_rnk_list_g.append(time.perf_counter() - start_time)
                ops_rnk.append(i)
        t_rank_list = time.perf_counter() - start_time
        
        log(f"{n:<12} | {'List':<12} | {t_insert_list:<16f} s | {t_select_list:<16f} s | {t_rank_list:<16f} s")
        
        
        # --- TEST ABR ---
        my_bst = ABR()
        t_ins_bst_g = []
        start_time = time.perf_counter()
        for i, val in enumerate(random_data, 1):
            my_bst.insert(val)
            if i % step_n == 0 or i == n: t_ins_bst_g.append(time.perf_counter() - start_time)
        t_insert_bst = time.perf_counter() - start_time
        
        t_sel_bst_g = []
        start_time = time.perf_counter()
        for i, idx in enumerate(search_indices, 1):
            my_bst.select(my_bst.root, idx)
            if i % step_s == 0 or i == num_selects: t_sel_bst_g.append(time.perf_counter() - start_time)
        t_select_bst = time.perf_counter() - start_time
        
        t_rnk_bst_g = []
        start_time = time.perf_counter()
        for i, k in enumerate(search_keys, 1):
            my_bst.rank(my_bst.root, k)
            if i % step_s == 0 or i == num_selects: t_rnk_bst_g.append(time.perf_counter() - start_time)
        t_rank_bst = time.perf_counter() - start_time
        
        log(f"{n:<12} | {'ABR':<12} | {t_insert_bst:<16f} s | {t_select_bst:<16f} s | {t_rank_bst:<16f} s")
        
        
        # --- TEST AVL ---
        my_avl = AVL()
        t_ins_avl_g = []
        start_time = time.perf_counter()
        for i, val in enumerate(random_data, 1):
            my_avl.insert(val)
            if i % step_n == 0 or i == n: t_ins_avl_g.append(time.perf_counter() - start_time)
        t_insert_avl = time.perf_counter() - start_time
        
        t_sel_avl_g = []
        start_time = time.perf_counter()
        for i, idx in enumerate(search_indices, 1):
            my_avl.select(idx)
            if i % step_s == 0 or i == num_selects: t_sel_avl_g.append(time.perf_counter() - start_time)
        t_select_avl = time.perf_counter() - start_time
        
        t_rnk_avl_g = []
        start_time = time.perf_counter()
        for i, k in enumerate(search_keys, 1):
            my_avl.rank(k)
            if i % step_s == 0 or i == num_selects: t_rnk_avl_g.append(time.perf_counter() - start_time)
        t_rank_avl = time.perf_counter() - start_time
        
        log(f"{n:<12} | {'AVL':<12} | {t_insert_avl:<16f} s | {t_select_avl:<16f} s | {t_rank_avl:<16f} s")
        log("-" * 90)

        for idx in range(len(ops_ins)):
            csv_insert_avg.append([n, ops_ins[idx], t_ins_list_g[idx], t_ins_bst_g[idx], t_ins_avl_g[idx]])

        for idx in range(len(ops_sel)):
            csv_select_avg.append([n, ops_sel[idx], t_sel_list_g[idx], t_sel_bst_g[idx], t_sel_avl_g[idx]])

        for idx in range(len(ops_rnk)):
            csv_rank_avg.append([n, ops_rnk[idx], t_rnk_list_g[idx], t_rnk_bst_g[idx], t_rnk_avl_g[idx]])


    # =========================================================
    # PARTE 2: CASO PEGGIORE (Costruzione Sequenziale)
    # =========================================================
    log("\n" + "="*60)
    log(f"CASO PEGGIORE: INSERIMENTO LINEARE ORDINATO")
    log("="*60)
    log(f"{'N Elements':<12} | {'Structure':<12} | {'Insert Time (Worst)':<20}")
    log("-"*60)

    for n in sizes:
        lista = List()
        t_list, t_list_g, ops_w = insert_linear_test(lista, n)
        log(f"{n:<12} | {'List':<12} | {t_list:<16f} s")

        abr = ABR()
        t_abr, t_abr_g, _ = insert_linear_test(abr, n)
        log(f"{n:<12} | {'ABR':<12} | {t_abr:<16f} s")

        avl = AVL()
        t_avl, t_avl_g, _ = insert_linear_test(avl, n)
        log(f"{n:<12} | {'AVL':<12} | {t_avl:<16f} s")
        log("-" * 60)

        for idx in range(len(ops_w)):
            csv_insert_worst.append([n, ops_w[idx], t_list_g[idx], t_abr_g[idx], t_avl_g[idx]])

    # =========================================================
    # SALVATAGGIO DEI DATI SU FILE (TXT E CSV)
    # =========================================================
    script_dir = os.path.dirname(__file__)
    data_dir = os.path.join(script_dir, '..', 'data')
    os.makedirs(data_dir, exist_ok=True)
    
    file_path = os.path.join(data_dir, "benchmark_results.txt")
    with open(file_path, "a", encoding="utf-8") as f:
        f.write("\n\n" + "\n".join(output_lines))
        
    def save_csv(filename, data_matrix):
        csv_path = os.path.join(data_dir, filename)
        with open(csv_path, mode='w', newline='', encoding='utf-8') as f_csv:
            writer = csv.writer(f_csv, delimiter=';')
            formatted_matrix = []
            for row in data_matrix:
                formatted_row = []
                for item in row:
                    if isinstance(item, float):
                        formatted_row.append(f"{item:.6f}".replace('.', ','))
                    else:
                        formatted_row.append(item)
                formatted_matrix.append(formatted_row)                
            writer.writerows(formatted_matrix)

    save_csv("dati_inserimento_casuale.csv", csv_insert_avg)
    save_csv("dati_select_casuale.csv", csv_select_avg)
    save_csv("dati_rank_casuale.csv", csv_rank_avg)
    save_csv("dati_inserimento_lineare.csv", csv_insert_worst)
        
    print(f"\n[INFO] Risultati completi (TXT) salvati in:\n{os.path.abspath(file_path)}")
    print(f"[INFO] 4 File CSV esportati con successo nella cartella /data per la generazione dei grafici.")


if __name__ == "__main__":
    print("\n" + "="*50)
    print("-- BENVENUTO NEL TESTER DI STATISTICHE D'ORDINE --")
    print("="*50)
    
    try:
        size = int(input("Con quanti elementi vuoi partire (n,2n,4n,8n)? "))
        num = int(input("Quanti elementi casuali vuoi cercare in ogni test? "))
        array_dinamico = [size, size * 2, size * 4, size * 8]
        
        print(f"\nAvvio dei test continui con N = {array_dinamico}...")
        run_all_benchmarks(num, array_dinamico)
        
    except ValueError:
        print("\n[ERRORE] Devi digitare dei numeri interi validi. Riprova.")