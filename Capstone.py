import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.ticker import MaxNLocator
# import plotly.express as px
# import plotly.graph_objects as go
import streamlit as st
from st_aggrid import GridOptionsBuilder, AgGrid, GridUpdateMode, DataReturnMode

# ------------------------------------------------------------------------------------------------------
st.set_page_config(page_title='Renewable Energy')

# ------------------------------------------------------------------------------------------------------
# st.title("Kebutuhan Energi Terbarukan di Indonesia")
st.markdown("<h1 style='text-align: center; color: blue;'>Kebutuhan Energi Terbarukan di Indonesia</h1>",
            unsafe_allow_html=True)
st.caption("by Kevin F Levandusky")
# image = 'https://drive.google.com/file/d/1qFnIu6VTp19aaWKZaWyH5VHejAGDxkEd/view?usp=sharing'
# url0 = 'https://drive.google.com/uc?id=' + image.split('/')[-2]
st.markdown("""---""")
st.markdown('## Ringkasan Eksekutif')
st.markdown('Per Agustus 2022, inflasi Indonesia masih di bawah rata-rata dunia. Namun perlu diperhatikan karena '
            'sejak Februari 2022, inflasi di seluruh dunia terus merangkak naik. Hal ini berpengaruh pada impor '
            'energi Indonesia. Untuk mengurangi impor energi tak terbarukan, Indonesia harus '
            'memperbanyak investasi di energi terbarukan, terutama di energi pembangkit tenaga air dan angin, '
            'karena potensi yang cukup besar mengingat disesuaikan dengan sumber daya yang ada (panjang garis '
            'pantai dan sungai). Energi terbarukan Indonesia saat ini sedang difokuskan pada energi geotermal.')
st.markdown("""---""")
# ------------------------------------------------------------------------------------------------------
st.markdown('# I. Pergerakan Indeks CPI')

# Tulisan 1
st.image('core-inflation.jpg', caption='Core inflation by Nick Youngson CC BY-SA 3.0')
st.markdown('Perang Invasi Rusia terhadap Ukraina yang terjadi sejak bulan Februari 2022, berdampak besar pada '
            'perekonomian dunia. Harga-harga mulai merangkak naik. Hal ini dapat dilihat dari inflasi yang mulai '
            'merangkak naik. Kurva Indeks Harga Konsumen (CPI) di sejumlah negara sudah mulai merangkak ke atas. '
            'Dapat dilihat pada gambar di bawah, **_terjadi kenaikan indeks CPI di bulan Februari 2022_** '
            '(pada garis putus-putus). **_Inflasi Indonesia_** (garis berwarna biru), '
            '**_sejak 2019, masih bisa bertahan_** di sekitaran pergerakan inflasi Asia Tenggara dan Asia Timur '
            '(garis berwarna biru muda), bahkan di bawah nilai persentase kenaikan Dunia (garis berwarna merah). '
            'Sejauh ini pergerakan inflasi rata-rata dunia masih sangat dipengaruhi oleh pergerakan inflasi '
            'dari negara-negara Eropa dan Amerika Utara. Hal ini terlihat dari bentuk pola bentuk turun naik garis. '
            'Pada saat Desember 2019 dan Januari 2020, semua inflasi naik, namun slope landai Dunia mirip seperti '
            'slope landai Eropa dan Amerika Utara. Berbeda dengan inflasi Asia Tenggara dan Timur yang slope-nya '
            'cukup curam, '
            'atau bahkan grafik Indonesia yang cenderung turun. Bahkan di awal tahun 2022, grafik Eropa-Amerika '
            'dengan Dunia hampir berhimpit. Salah satu faktor ini kemungkinan besar penggunaan mata uang pembelian '
            'barang-barang masih menggunakan mata uang negara di Eropa dan Amerika. ')

# ------------------------------------------------------------------------------------------------------
# Ambil Data dan Tabel ------------> Gambar 1
# data_inflation = 'https://drive.google.com/file/d/1u4WIgaMISery5PuAq9tHEq_A0h2kb4aO/view?usp=sharing'
# url1 = 'https://drive.google.com/uc?id=' + data_inflation.split('/')[-2]
df1 = pd.read_csv('data_inflation.csv')
df1 = df1.set_index('No')
fig1, ax1 = plt.subplots(1, 1, figsize=(12, 7))
# fig11, ax11 = go.Figure()
# fig11.add_trace(go.Scatter)
ax1.set_title("Data Inflation CPI\n", fontsize=24)
colors1 = ["darkblue", "tab:gray", "tab:cyan", "tab:pink", "tab:red"]
line_widths1 = [6, 2.1, 3, 2.1, 3]
lp1 = df1.plot(x='Period', kind="line", ax=ax1, ylim=[-0.3, 12], color=colors1, yticks=[0, 2, 4, 6, 8, 10, 12])
add_lbl_pos1 = [0.5, 1.0, -0.1, -0.3, 0.5]

# Gambar garis
for i, item in enumerate(lp1.get_lines()):
    item.set_linewidth(line_widths1[i])
    lbl = item.get_label()
    ax1.annotate(lbl, (38, df1.loc[df1['Period'] == 'Mar-22', lbl]),
                 (41, df1.loc[df1['Period'] == 'Mar-22', lbl] + add_lbl_pos1[i]),
                 fontweight="bold", fontsize=12, color=colors1[i], va="center",
                 arrowprops={"arrowstyle": "-", "color": colors1[i]})

fig1.supxlabel('Sumber: Bank Indonesia, akses: 1 Oct 22 dan https://ilostat.ilo.org, akses: 8 Oct 22',
               x=0.3, y=0, size=10)
ax1.set_xlabel("Periode", fontsize=14)
ax1.set_ylabel("Persentase (%)\n", fontsize=14)
ax1.axvline(x=37, linestyle='--', color='r')
ax1.text(36.9, 12, 'Perang Rusia\n- Ukraina', color='r', ha='right', va='top')
ax1.get_legend().remove()
ax1.grid(True, which='both')
# plt.tight_layout(rect=(0, 0, 1, 0.90))
st.pyplot(fig1)

# ------------------------------------------------------------------------------------------------------
st.markdown('Sementara pada bulan Agustus 2022, inflasi Indonesia **_sudah mulai naik ke nilai 5 hingga 6 persen._** '
            'Kenaikan persentase inflasi CPI Indonesia sudah mulai di atas Asia Tenggara dan Timur sejak '
            'awal tahun 2022, dan terus merangkak naik, meskipun masih jauh dibawah persentase dunia. '
            'Meskipun nilai ini masih di bawah nilai Indeks Dunia, namun Indonesia harus mulai hati-hati. '
            'Kehati-hatian ini didasarkan karena besaran inflasi akan berpengaruh pada kekuatan nilai Rupiah '
            'terhadap mata uang asing terutama Dollar. Jika nilai Rupiah tertekan, maka nilai impor Indonesia '
            'terhadap mata uang asing akan naik.')
st.markdown('Salah satu impor terbesar Indonesia yaitu impor energi/migas. Dan '
            'sektor yang mengonsumsi energi terbesar di tahun 2021 yaitu sektor transportasi, sebesar '
            '388,42 juta BOE (Barrel Oil Equivalent) atau 42,72% dari total konsumsi energi nasional *(1). '
            'Sehingga, sebagian bahan bakar minyak yang merupakan hasil impor menjadi salah satu sektor subsidi '
            'terbesar di Indonesia. Apabila Rupiah tertekan, hal ini akan sangat membebani APBN negara, karena nilai '
            'impor akan menjadi semakin mahal, karena membeli dengan menggunakan Dollar '
            'Per tanggal 12 Oktober 2022, **_nilai Rupiah terhadap Dollar sudah mencapai Rp15.300/USD._** '
            'Apabila hal ini terus bertahan, maka neraca energi APBN Indonesia akan menjadi defisit. Oleh karena itu, '
            'harus ada perubahan/perbaikan kebijakan mengenai subsidi energi ini kedepannya.')
st.markdown("""---""")

# ------------------------------------------------------------------------------------------------------
st.markdown('# II. Energi dan Energi Terbarukan')
st.image('renewable_energy.jpg', caption='Renewable Energy Development in the California Desert '
                                         'by mypubliclands is licensed under CC BY 2.0.')
# Tulisan 2
st.markdown("Melansir dari Handbook of Energy & Economic Statistics of Indonesia 2021, "
            "energi yang dihasilkan tahun 2021 yaitu sebesar 1,545,557,232 BOE (Barrel Oil Equivalent) "
            "atau sekitar 2626.58 Terawatt Hour. Sementara energi yang digunakan atau dikonsumsi tahun 202i "
            "yaitu sebesar 909,244,973 BOE atau sekitar 1545.21 Terawatt Hour. Hal ini menjadi hal positif "
            "untuk ketahanan energi Indonesia dimana **_Indonesia masih bisa surplus di bidang ketahanan energi._** "
            "Namun Indonesia harus tetap berhati-hati. Faktor surplus tersebut, **_kemungkinan dikarenakan tahun 2021 "
            "masih merupakan tahun perbaikan/penyesuaian akibat wabah Covid-19_**, dimana belum sepenuhnya energi "
            "dibutuhkan oleh masyarakat diantaranya masih adanya WFH di berbagai kota, sehingga kebutuhan "
            "transportasi masih rendah, dan sebagainya.")

# ------------------------------------------------------------------------------------------------------
# Ambil Data dan Tabel ------------> Gambar 2
df2 = pd.read_csv('primary_energy_source_bar.csv')
df2 = df2[(df2['Year'] >= 2000)]  # lebih besar dari tahun 2000
df2_1 = df2[(df2['Entity'] == 'Indonesia')].tail(10).reset_index().drop(['index', 'Code'], axis=1)

# ------------------------------------------------------------------------------------------------------
st.markdown('Pembagian jenis energi yang digunakan oleh Indonesia dapat dilihat pada tabel di bawah ini. '
            'Dapat terlihat bahwa masih besar angka penggunaan luaran energi dari sumber daya tidak terbarukan '
            '(Non renewable). Sementara jumlah penggunaan dari sumber daya terbarukan (renewable) masih cukup sedikit. '
            'Dari surplus energi tahun lalu, ada baiknya Indonesia memulai perlahan-lahan untuk melakukan '
            'perubahan energi dari non renewable menjadi renewable energi. ')
st.markdown('Berikut ini tabel penggunaan energi dari berbagai negara: (untuk melihat pilih negaranya dan klik update)')

# ------------------------------------------------------------------------------------------------------
gb = GridOptionsBuilder.from_dataframe(df2.drop(['Code'], axis=1))
gb.configure_pagination(paginationAutoPageSize=True)  # Add pagination
gb.configure_side_bar()  # Add a sidebar
gb.configure_selection('multiple', use_checkbox=True,
                       groupSelectsChildren="Group checkbox select children")  # Enable multi-row selection
gridOptions = gb.build()

grid_response = AgGrid(
    df2.drop(['Code'], axis=1),
    gridOptions=gridOptions,
    data_return_mode=DataReturnMode.FILTERED,
    update_mode=GridUpdateMode.MANUAL,
    fit_columns_on_grid_load=False,
    theme='alpine',  # Add theme color to the table
    enable_enterprise_modules=True,
    height=350,
    width='100%',
    reload_data=False,
)

df2 = grid_response['data']
selected = grid_response['selected_rows']
df2_0 = pd.DataFrame(selected)
st.table(df2_0)
st.markdown('Dari gambar di bawah ini, jika dibandingkan dengan negara lain, konsumsi energi yang '
            'digunakan oleh Indonesia (warna biru, gambar bawah) termasuk nilai yang cukup kecil. '
            'Sebagai informasi, negara dengan konsumsi batubara/coal dan minyak/oil yang terbesar yaitu '
            'Amerika Serikat menggunakan energi dari oil dan batubara masing-masing mencapai diatas 10000 '
            'dan 6000 TWh. Begitu pula untuk energi terbarukan, '
            'dimana Indonesia juga menggunakan energi yang cukup rendah jika dibandingkan dengan negara pengonsumsi '
            'renewable energy terbesar yaitu China. Perbandingan Indonesia dengan keseluruhan '
            'negara dapat dilihat pada gambar di bawah ini, dimana Indonesia ditandai dengan warna biru.')

# ------------------------------------------------------------------------------------------------------
df2['Country_Code'] = 0.4  # untuk area scatter
df2 = df2[df2['Entity'] \
              .str.contains("World|High-income countries|Non-OECD (BP)|OECD (BP)|Asia|Asia Pacific (BP)|"
                            "Upper-middle-income countries|North America|North America (BP)|Europe|"
                            "European Union (27)|Lower-middle-income countries|Middle East (BP)|"
                            "South and Central America (BP)|South America|CIS (BP)|Africa (BP)|Africa|"
                            "Other Africa (BP)") == False]
df2.loc[df2.Entity == 'Indonesia', 'Country_Code'] = 15
fig2_1, ax2_1 = plt.subplots(1, 1, figsize=(7, 4))
fig2_2, ax2_2 = plt.subplots(1, 1, figsize=(7, 4))
fig2_3, ax2_3 = plt.subplots(1, 1, figsize=(7, 4))
fig2_4, ax2_4 = plt.subplots(1, 1, figsize=(7, 4))
fig2_5, ax2_5 = plt.subplots(1, 1, figsize=(7, 4))
fig2_6, ax2_6 = plt.subplots(1, 1, figsize=(7, 4))
# (ax2_1, ax2_2, ax2_3, ax2_4, ax2_5, ax2_6) = axs2
area2 = df2['Country_Code']
colors2 = {0.4: 'gray', 15: 'blue'}
ax2_1.scatter(x=df2['Year'], y=df2['Coal Consumption - TWh'], s=area2, color=df2['Country_Code'].map(colors2))
ax2_1.set_title('Coal', fontsize=11)
ax2_2.scatter(x=df2['Year'], y=df2['Oil Consumption - TWh'], s=area2, color=df2['Country_Code'].map(colors2))
ax2_2.set_title('Oil', fontsize=11)
ax2_3.scatter(x=df2['Year'], y=df2['Hydro Consumption - TWh'], s=area2, color=df2['Country_Code'].map(colors2))
ax2_3.set_title('Hydro', fontsize=11)
ax2_4.scatter(x=df2['Year'], y=df2['Wind Consumption - TWh'], s=area2, color=df2['Country_Code'].map(colors2))
ax2_4.set_title('Wind', fontsize=11)
ax2_5.scatter(x=df2['Year'], y=df2['Solar Consumption - TWh'], s=area2, color=df2['Country_Code'].map(colors2))
ax2_5.set_title('Solar', fontsize=11)
ax2_6.scatter(x=df2['Year'], y=df2['Geo Biomass Other - TWh'], s=area2, color=df2['Country_Code'].map(colors2))
ax2_6.set_title('Other', fontsize=11)
fig2_1.suptitle("Energi yang Dikonsumsi Berdasarkan Jenis Sumber Daya", fontsize=14)
fig2_1.supylabel('Energi Luaran (TeraWattHour)', fontsize=12)
fig2_1.supxlabel('Tahun\n\n'
                 'Sumber: https://ourworldindata.org/energy, akses: 24 Sep 22', x=0.5, y=0.02, size=10)
fig2_1.tight_layout()
fig2_2.suptitle("Energi yang Dikonsumsi Berdasarkan Jenis Sumber Daya", fontsize=14)
fig2_2.supylabel('Energi Luaran (TeraWattHour)', fontsize=12)
fig2_2.supxlabel('Tahun\n\n'
                 'Sumber: https://ourworldindata.org/energy, akses: 24 Sep 22', x=0.5, y=0.02, size=10)
fig2_2.tight_layout()
fig2_3.suptitle("Energi yang Dikonsumsi Berdasarkan Jenis Sumber Daya", fontsize=14)
fig2_3.supylabel('Energi Luaran (TeraWattHour)', fontsize=12)
fig2_3.supxlabel('Tahun\n\n'
                 'Sumber: https://ourworldindata.org/energy, akses: 24 Sep 22', x=0.5, y=0.02, size=10)
fig2_3.tight_layout()
fig2_4.suptitle("Energi yang Dikonsumsi Berdasarkan Jenis Sumber Daya", fontsize=14)
fig2_4.supylabel('Energi Luaran (TeraWattHour)', fontsize=12)
fig2_4.supxlabel('Tahun\n\n'
                 'Sumber: https://ourworldindata.org/energy, akses: 24 Sep 22', x=0.5, y=0.02, size=10)
fig2_4.tight_layout()
fig2_5.suptitle("Energi yang Dikonsumsi Berdasarkan Jenis Sumber Daya", fontsize=14)
fig2_5.supylabel('Energi Luaran (TeraWattHour)', fontsize=12)
fig2_5.supxlabel('Tahun\n\n'
                 'Sumber: https://ourworldindata.org/energy, akses: 24 Sep 22', x=0.5, y=0.02, size=10)
fig2_5.tight_layout()
fig2_6.suptitle("Energi yang Dikonsumsi Berdasarkan Jenis Sumber Daya", fontsize=14)
fig2_6.supylabel('Energi Luaran (TeraWattHour)', fontsize=12)
fig2_6.supxlabel('Tahun\n\n'
                 'Sumber: https://ourworldindata.org/energy, akses: 24 Sep 22', x=0.5, y=0.02, size=10)
fig2_6.tight_layout()
# st.pyplot(fig2, clear_figure=False)
tab2_1, tab2_2, tab2_3, tab2_4, tab2_5, tab2_6 = st.tabs(["Batubara", "Minyak", 'Air', ' Angin', 'Surya', 'Lainnya'])
tab2_1.pyplot(fig2_1)
tab2_2.pyplot(fig2_2)
tab2_3.pyplot(fig2_3)
tab2_4.pyplot(fig2_4)
tab2_5.pyplot(fig2_5)
tab2_6.pyplot(fig2_6)

# ------------------------------------------------------------------------------------------------------
st.markdown('Energi yang digunakan dan dikonsumsi Indonesia memang terlihat tidak besar dibandingkan negara '
            'lain dan tidak berpengaruh besar secara nilainya. Ini berpengaruh pada pengelolaan penggunaan energi '
            'di Indonesia. Namun sayangnya Indonesia merupakan negara yang belum baik dalam mengelola sumber daya '
            'energi. Hal ini tercermin pada peringkat ketahanan energi Indonesia di dunia. Pada tahun 2014, '
            'Indonesia berada pada peringkat ke-69 dari 129 negara. Meski demikian, belakangan ini peringkat '
            'Indonesia dalam ketahanan energi semakin baik. **_Pada tahun 2021, World Energy Council '
            'menetapkan Indonesia menduduki peringkat ke 56 dari 100 negara_** dalam hal ketahanan energi nasional. '
            'Hal ini menunjukkan semakin membaiknya perbaikan pengelolaan energi. Seharusnya semakin baiknya '
            'pengelolaan energi, harus diimbangi dengan perlindungan terhadap lingkungan hidup. Hal ini agar sesuai '
            'dengan Kebijakan Energi Nasional PP No. 79 Tahun 2014. Selain itu juga demi menuju transisi energi dan '
            'net zero emission di tahun 2060 *(2).')
st.markdown('Jika melihat dari data persentase energi terbarukan Indonesia masih sangat rendah. Indonesia hampir '
            'tidak pernah di atas rata-rata dunia sejak tahun 1970. Hal ini perlu diperbaiki apabila Indonesia '
            'masih ingin mengejar net zero emission, dimana net zero emission umumnya dihasilkan oleh energi '
            'yang berasal dari Karbon, seperti batubara dan minyak.')

# ------------------------------------------------------------------------------------------------------
# Ambil Data dan Tabel ------------> Gambar 3
# renewable_share_energy = 'https://drive.google.com/file/d/1ZTMqQiciLIXnxJ7rni4kPHmMQKZ65QhA/view?usp=sharing'
# url3 = 'https://drive.google.com/uc?id=' + renewable_share_energy.split('/')[-2]
df3 = pd.read_csv('renewable_share_energy.csv')
df3.rename({'Renewables (% equivalent primary energy)': '%Renewable'}, axis='columns', inplace=True)
df3topcountry = (df3.groupby(['Entity'])['%Renewable']
                 .max()
                 .reset_index()
                 .sort_values(by='%Renewable', ascending=False)
                 .head(5))
df3_pilihan = df3[df3['Entity'].str.contains("Norway|Indonesia|Iceland|World|Turkey") == True]
df3_1 = pd.concat([df3topcountry, df3_pilihan])
fig3, ax3 = plt.subplots(1, 1, figsize=(14, 7))
colors3 = ["tab:pink", "darkblue", "tab:cyan", "tab:gray", "tab:red"]
df3_1.groupby(['Year', 'Entity'])['%Renewable'].sum().unstack().plot(kind='line', ax=ax3, marker='.', color=colors3)
ax3.annotate('Iceland', xy=(2020, 86),
             xytext=(2020, 93),
             fontweight="bold", fontsize=12, color='tab:pink', va="center",
             arrowprops={"arrowstyle": "-", "color": 'tab:pink'})
ax3.annotate('Indonesia', xy=(2020, 10),
             xytext=(2020, 1),
             fontweight="bold", fontsize=12, color='darkblue', va="center",
             arrowprops={"arrowstyle": "-", "color": 'darkblue'})
ax3.annotate('Norwegia', xy=(2020, 71),
             xytext=(2020, 65),
             fontweight="bold", fontsize=12, color='tab:cyan', va="center",
             arrowprops={"arrowstyle": "-", "color": 'tab:cyan'})
ax3.annotate('Turki', xy=(2020, 19),
             xytext=(2020, 24),
             fontweight="bold", fontsize=12, color='tab:gray', va="center",
             arrowprops={"arrowstyle": "-", "color": 'tab:gray'})
ax3.annotate('World', xy=(2021, 13),
             xytext=(2023, 11),
             fontweight="bold", fontsize=12, color='tab:red', va="center",
             arrowprops={"arrowstyle": "-", "color": 'tab:red'})

plt.title('Besaran Persentase Penggunaan Energi Terbarukan', loc='center', pad=30, fontsize=20, color='blue')
ax3.set_xlabel('Tahun', fontsize=13.5)
ax3.set_ylabel('Konsumsi Energi Terbarukan/\nKonsumsi Seluruh Energi (%)\n', fontsize=13.5)
# ax3.legend(loc='upper right', bbox_to_anchor=(1.1, 1), shadow=True, ncol=1)
ax3.get_legend().remove()
fig3.supxlabel('Sumber: https://ourworldindata.org/energy, akses: 24 Sep 22', x=0.26, y=0.02, size=12)
st.pyplot(fig3)

# ------------------------------------------------------------------------------------------------------
st.markdown('Indonesia cukup jauh tertinggal dibandingkan **_negara-negara Skandinavia_**, dimana rata-rata negara '
            'tersebut sudah **_memiliki sumber renewable energy di atas 50 persen_**. Bahkan negara yang memiliki '
            'GDP setingkat Indonesia, Turki sudah memiliki persentase renewable energi di atas Indonesia. '
            'Hal ini mungkin disebabkan oleh fokus Turki melalui Eleventh Development Plan (2019-2023) untuk '
            'dapat menghasilkan/ menggunakan energi terbarukan sebesar 38.8% *(3). ')
st.markdown('Namun Indonesia (grafik warna biru) sudah mulai bergerak menanjak ke atas sejak tahun 2014. '
            'Hal ini salah satunya merupakan dampak dari Kebijakan Energi Nasional yang telah dimulai pada tahun '
            'yang sama. Meskipun sudah mulai naik nilai persentase penggunaan energi terbarukan, namun masih perlu '
            'lebih banyak investasi dan pergerakan uang untuk energi terbarukan. Grafik di bawah ini menunjukkan '
            'besaran capital yang berhubungan dengan sumber energi renewable, baik investasi ataupun pergerakan nilai '
            'uang yang berhubungan dengan Renewable Energy. Kita akan membandingkan dengan negara Brazil karena '
            'negara tersebut sedang menginvestasikan pada energi terbarukan dengan nilai cukup besar.')

# ------------------------------------------------------------------------------------------------------
# Ambil Data dan Tabel ------------> Gambar 4
# table_invest_final = 'https://drive.google.com/file/d/1ZTMqQiciLIXnxJ7rni4kPHmMQKZ65QhA/view?usp=sharing'
# url4 = 'https://drive.google.com/uc?id=' + table_invest_final.split('/')[-2]
df4 = pd.read_csv('table_invest_final.csv')
df4.rename({'Country/area': 'Country', 'Public Flows (2020 USD M)': 'Public Flows'}, axis='columns', inplace=True)
df4['Country_Code'] = 3  # untuk luas scatter
df4.loc[df4.Country == 'Brazil', 'Country_Code'] = 30  # untuk luas scatter
df4.loc[df4.Country == 'Indonesia', 'Country_Code'] = 35  # untuk luas scatter
# df4 = df4[df4['Technology'].str.contains("Coal and Peat|Fossil fuels n.e.s.
# |Oil|Non-renewable municipal waste|Nuclear") == False]

fig4_1, ax4_1 = plt.subplots(1, 1, figsize=(7, 4))
fig4_2, ax4_2 = plt.subplots(1, 1, figsize=(7, 4))
fig4_3, ax4_3 = plt.subplots(1, 1, figsize=(7, 4))
fig4_4, ax4_4 = plt.subplots(1, 1, figsize=(7, 4))
fig4_5, ax4_5 = plt.subplots(1, 1, figsize=(7, 4))
fig4_6, ax4_6 = plt.subplots(1, 1, figsize=(7, 4))
# (ax4_1, ax4_2, ax4_3, ax4_4, ax4_5, ax4_6) = axs4
colors4 = {3: 'black', 30: 'red', 35: 'blue'}

ax4_1.scatter(x=df4.loc[df4['Technology'] == 'Solar photovoltaic', ['Year']],
              y=df4.loc[df4['Technology'] == 'Solar photovoltaic', ['Public Flows']],
              s=df4.loc[df4['Technology'] == 'Solar photovoltaic', ['Country_Code']],
              color=df4.loc[df4['Technology'] == 'Solar photovoltaic', ['Country_Code']].squeeze().map(colors4))
ax4_1.set_title('Solar photovoltaic', fontsize=13)
ax4_1.xaxis.set_major_locator(MaxNLocator(integer=True))
ax4_2.scatter(x=df4.loc[df4['Technology'] == 'Onshore wind energy', ['Year']],
              y=df4.loc[df4['Technology'] == 'Onshore wind energy', ['Public Flows']],
              s=df4.loc[df4['Technology'] == 'Onshore wind energy', ['Country_Code']],
              color=df4.loc[df4['Technology'] == 'Onshore wind energy', ['Country_Code']].squeeze().map(colors4))
ax4_2.set_title('Onshore wind energy', fontsize=13)
ax4_2.xaxis.set_major_locator(MaxNLocator(integer=True))
ax4_3.scatter(x=df4.loc[df4['Technology'] == 'Renewable hydropower', ['Year']],
              y=df4.loc[df4['Technology'] == 'Renewable hydropower', ['Public Flows']],
              s=df4.loc[df4['Technology'] == 'Renewable hydropower', ['Country_Code']],
              color=df4.loc[df4['Technology'] == 'Renewable hydropower', ['Country_Code']].squeeze().map(colors4))
ax4_3.set_title('Renewable hydropower', fontsize=13)
ax4_3.xaxis.set_major_locator(MaxNLocator(integer=True))
ax4_4.scatter(x=df4.loc[df4['Technology'] == 'Geothermal energy', ['Year']],
              y=df4.loc[df4['Technology'] == 'Geothermal energy', ['Public Flows']],
              s=df4.loc[df4['Technology'] == 'Geothermal energy', ['Country_Code']],
              color=df4.loc[df4['Technology'] == 'Geothermal energy', ['Country_Code']].squeeze().map(colors4))
ax4_4.set_title('Geothermal energy', fontsize=13)
ax4_4.xaxis.set_major_locator(MaxNLocator(integer=True))
ax4_5.scatter(x=df4.loc[df4['Technology'] == 'Renewable municipal waste', ['Year']],
              y=df4.loc[df4['Technology'] == 'Renewable municipal waste', ['Public Flows']],
              s=df4.loc[df4['Technology'] == 'Renewable municipal waste', ['Country_Code']],
              color=df4.loc[df4['Technology'] == 'Renewable municipal waste', ['Country_Code']].squeeze().map(colors4))
ax4_5.set_title('Renewable municipal waste', fontsize=13)
ax4_5.xaxis.set_major_locator(MaxNLocator(integer=True))
ax4_6.scatter(x=df4.loc[df4['Technology'] == 'Multiple renewables', ['Year']],
              y=df4.loc[df4['Technology'] == 'Multiple renewables', ['Public Flows']],
              s=df4.loc[df4['Technology'] == 'Multiple renewables', ['Country_Code']],
              color=df4.loc[df4['Technology'] == 'Multiple renewables', ['Country_Code']].squeeze().map(colors4))
ax4_6.set_title('Other', fontsize=11)
ax4_6.xaxis.set_major_locator(MaxNLocator(integer=True))
# handles, labels = [(a + b) for a, b in zip(axs4.get_legend_handles_labels(), axs2.get_legend_handles_labels())]
fig4_1.legend(['Legend:\nMerah = Brazil\nBiru = Indonesia'], loc=(0.79, 0.8), fontsize=8)
fig4_2.legend(['Legend:\nMerah = Brazil\nBiru = Indonesia'], loc=(0.79, 0.8), fontsize=8)
fig4_3.legend(['Legend:\nMerah = Brazil\nBiru = Indonesia'], loc=(0.79, 0.8), fontsize=8)
fig4_4.legend(['Legend:\nMerah = Brazil\nBiru = Indonesia'], loc=(0.79, 0.8), fontsize=8)
fig4_5.legend(['Legend:\nMerah = Brazil\nBiru = Indonesia'], loc=(0.79, 0.8), fontsize=8)
fig4_6.legend(['Legend:\nMerah = Brazil\nBiru = Indonesia'], loc=(0.79, 0.8), fontsize=8)
fig4_1.suptitle("Besaran Pergerakan Capital\nEnergi Terbarukan", fontsize=18)
fig4_2.suptitle("Besaran Pergerakan Capital\nEnergi Terbarukan\n", fontsize=18)
fig4_3.suptitle("Besaran Pergerakan Capital\nEnergi Terbarukan\n", fontsize=18)
fig4_4.suptitle("Besaran Pergerakan Capital\nEnergi Terbarukan\n", fontsize=18)
fig4_5.suptitle("Besaran Pergerakan Capital\nEnergi Terbarukan\n", fontsize=18)
fig4_6.suptitle("Besaran Pergerakan Capital\nEnergi Terbarukan\n", fontsize=18)
fig4_1.supylabel('Nilai Capital / Investasi\n(USD juta)', fontsize=16, ha='center')
fig4_2.supylabel('Nilai Capital / Investasi\n(USD juta)', fontsize=16, ha='center')
fig4_3.supylabel('Nilai Capital / Investasi\n(USD juta)', fontsize=16, ha='center')
fig4_4.supylabel('Nilai Capital / Investasi\n(USD juta)', fontsize=16, ha='center')
fig4_5.supylabel('Nilai Capital / Investasi\n(USD juta)', fontsize=16, ha='center')
fig4_6.supylabel('Nilai Capital / Investasi\n(USD juta)', fontsize=16, ha='center')
fig4_1.supxlabel('Sumber: https://pxweb.irena.org/pxweb/en/IRENASTAT, akses: 8 Oct 22', x=0.35, y=0.02, size=10)
fig4_2.supxlabel('Sumber: https://pxweb.irena.org/pxweb/en/IRENASTAT, akses: 8 Oct 22', x=0.35, y=0.02, size=10)
fig4_3.supxlabel('Sumber: https://pxweb.irena.org/pxweb/en/IRENASTAT, akses: 8 Oct 22', x=0.35, y=0.02, size=10)
fig4_4.supxlabel('Sumber: https://pxweb.irena.org/pxweb/en/IRENASTAT, akses: 8 Oct 22', x=0.35, y=0.02, size=10)
fig4_5.supxlabel('Sumber: https://pxweb.irena.org/pxweb/en/IRENASTAT, akses: 8 Oct 22', x=0.35, y=0.02, size=10)
fig4_6.supxlabel('Sumber: https://pxweb.irena.org/pxweb/en/IRENASTAT, akses: 8 Oct 22', x=0.35, y=0.02, size=10)
fig4_1.tight_layout()
fig4_2.tight_layout()
fig4_3.tight_layout()
fig4_4.tight_layout()
fig4_5.tight_layout()
fig4_6.tight_layout()
# st.pyplot(fig4)

tab4_1, tab4_2, tab4_3, tab4_4, tab4_5, tab4_6 = st.tabs(["Energi Surya", "Energi Angin",
                                                          'Energi Air', 'Energi Geothermal',
                                                          'Energi Limbah', 'Lainnya'])
tab4_1.pyplot(fig4_1)
tab4_2.pyplot(fig4_2)
tab4_3.pyplot(fig4_3)
tab4_4.pyplot(fig4_4)
tab4_5.pyplot(fig4_5)
tab4_6.pyplot(fig4_6)

st.markdown('Jika dibandingkan dengan negara Brazil, salah satu negara yang serius dalam mengembangkan '
            'energi terbarukan, Indonesia masih dibawah Brazil dalam public flow untuk renewable energy. '
            'Ada beberapa kemungkinan alasan. Pertama nilai GDP Brazil yang di atas Indonesia. Kedua, luas '
            'sumber daya yang dapat dimanfaatkan (seperti hydropower di sungai Amazon, atau tenaga angin yang '
            'dapat diletakkan di garis pantai. Namun Indonesia juga seharusnya mampu membuat hal serupa. '
            'Garis pantai Indonesia cukup panjang, sekitar 95.181 km dimana dapat digunakan untuk mendapatkan '
            'daya dari hasil angin laut, dan memiliki garis sungai yang cukup panjang. Meskipun demikian, '
            'untuk saat ini memang Indonesia lebih memfokuskan pada penggunaan energi geotermal. Ini terlihat '
            'pada gambar di bagian geotermal.')
st.markdown('Indonesia sendiri sedang memfokuskan pada energi geotermal. Ini terlihat dari pergerakan uang yang '
            'bergerak pada jenis energi ini. Selain itu, penggunaan energi dari limbah belum terlihat sama sekali '
            '(atau mungkin belum terdata). Sementara beberapa negara sudah mulai menggunakan energi dari pembuangan '
            'limbah, seperti Finlandia dan Perancis. Kedepannya dimana produksi limbah Indonesia yang cukup besar, '
            'diharapkan Indonesia mampu menggunakan teknologi dengan memanfaatkan energi yang dihasilkan dari '
            'limbah tersebut.')
# ------------------------------------------------------------------------------------------------------
st.subheader('Penutup')
st.markdown('Dari data-data yang telah dipaparkan di atas, ada beberapa kesimpulan yang dapat diambil berkaitan '
            'energi terbarukan. Pertama, penggunaan energi tidak terbarukan dapat mulai dikurangi. Hal ini dapat '
            'meringankan nilai impor Indonesia terhadap asing. Kedua, investasi untuk beberapa area pembangkit '
            'dapat ditingkatkan, seperti pembangkit energi tenaga surya, dan energi pembangkit tenaga angin. Selain '
            'itu, sumber energi dari limbah mulai dapat diekplorasi karena cukup banyaknya limbah Indonesia. Oleh '
            'karena itu, kedepannya diharapkan Indonesia mampu mencapai tantangan zero emission di tahun 2060. '
            'Komitmen dan peran serta pemerintah dan masyarakatlah yang mampu menjawab tantangan tersebut.')
# ------------------------------------------------------------------------------------------------------
st.markdown("""---""")
'Referensi :'
st.markdown('1. https://www.esdm.go.id/assets/media/content/content-handbook-of-energy-and-economic-statistics-of-'
            'indonesia-2021.pdf, akses 13 Oktober 2022.')
'2. https://suarakarya.co.id/indonesia-duduki-peringkat-ke-56-ketahanan-energi/35469/, akses 13 Oktober 2022.'
'3. https://www.iea.org/reports/turkey-2021, akses: 14 Oktober 2022.'
