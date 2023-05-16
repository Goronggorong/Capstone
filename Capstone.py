import pandas as pd
import matplotlib.pyplot as plt
# from matplotlib.ticker import MaxNLocator
# import seaborn as sns
from plotly import express as px
# import plotly.graph_objects as go
import streamlit as st
from st_aggrid import GridOptionsBuilder, AgGrid, GridUpdateMode, DataReturnMode


# ------------------------------------------------------------------------------------------------------
st.set_page_config(page_title='Renewable Energy')
selected_option = st.sidebar.selectbox("Select language", ["Bahasa Indonesia", "English"])

# ------------------------------------------------------------------------------------------------------
# st.title("Kebutuhan Energi Terbarukan di Indonesia")
if selected_option == "Bahasa Indonesia":
    st.markdown("<h1 style='text-align: center; color: #0073FF;'>Kebutuhan Energi Terbarukan di Indonesia</h1>",
                unsafe_allow_html=True)
    st.caption("oleh Kevin F Levandusky")
elif selected_option == "English":
    st.markdown("<h1 style='text-align: center; color: #0073FF;'>Renewable Energy Needs in Indonesia</h1>",
                unsafe_allow_html=True)
    st.caption("by Kevin F Levandusky")
# image = 'https://drive.google.com/file/d/1qFnIu6VTp19aaWKZaWyH5VHejAGDxkEd/view?usp=sharing'
# url0 = 'https://drive.google.com/uc?id=' + image.split('/')[-2]
st.markdown("""---""")
if selected_option == "Bahasa Indonesia":
    st.markdown('## Ringkasan Eksekutif')
    st.markdown('Per Agustus 2022, inflasi Indonesia masih di bawah rata-rata dunia. Namun perlu diperhatikan karena '
                'sejak Februari 2022, inflasi di seluruh dunia terus merangkak naik. Hal ini berpengaruh pada impor '
                'energi Indonesia. Untuk mengurangi impor energi tak terbarukan, Indonesia harus '
                'memperbanyak investasi di energi terbarukan, terutama di energi pembangkit tenaga air dan angin, '
                'karena potensi yang cukup besar mengingat disesuaikan dengan sumber daya yang ada (panjang garis '
                'pantai dan sungai). Energi terbarukan Indonesia saat ini sedang difokuskan pada energi geotermal.')
elif selected_option == "English":
    st.markdown('## Executive Summary')
    st.markdown("As of August 2022, Indonesia's inflation rate remains below the global average. However, "
                "it should be noted that since February 2022, inflation worldwide has been steadily increasing. "
                "This has an impact on Indonesia's energy imports. To reduce reliance on non-renewable energy imports, "
                "Indonesia needs to increase investments in renewable energy, particularly in hydropower and "
                "wind power, considering the significant potential based on available resources (coastline length "
                "and rivers). Currently, Indonesia is focusing on geothermal energy as a renewable energy source.")
st.markdown("""---""")
# ------------------------------------------------------------------------------------------------------
if selected_option == "Bahasa Indonesia":
    st.markdown('# I. Pergerakan Indeks CPI')
elif selected_option == "English":
    st.markdown('# I. CPI Index Movement')

# Tulisan 1
st.image('core-inflation.jpg', caption='Core inflation by Nick Youngson CC BY-SA 3.0')
if selected_option == "Bahasa Indonesia":
    st.markdown('Perang Invasi Rusia terhadap Ukraina yang terjadi sejak bulan Februari 2022, berdampak besar pada '
                'perekonomian dunia. Harga-harga mulai merangkak naik. Hal ini dapat dilihat dari inflasi yang mulai '
                'merangkak naik. Kurva Indeks Harga Konsumen (CPI) di sejumlah negara sudah mulai merangkak ke atas. '
                'Dapat dilihat pada gambar di bawah, **_terjadi kenaikan indeks CPI di bulan Februari 2022_** '
                '(pada garis putus-putus). **_Inflasi Indonesia_** (garis berwarna biru), '
                '**_sejak 2019, masih bisa bertahan_** di sekitaran pergerakan inflasi Asia Tenggara dan Asia Timur '
                '(garis berwarna biru muda), bahkan di bawah nilai persentase kenaikan Dunia (garis berwarna merah). '
                'Sejauh ini pergerakan inflasi rata-rata dunia masih sangat dipengaruhi oleh pergerakan inflasi '
                'dari negara-negara Eropa dan Amerika Utara. Hal ini terlihat dari bentuk pola bentuk turun naik '
                'garis. Pada saat Desember 2019 dan Januari 2020, semua inflasi naik, namun slope landai Dunia mirip '
                'seperti slope landai Eropa dan Amerika Utara. Berbeda dengan inflasi Asia Tenggara dan Timur '
                'yang slope-nya cukup curam, '
                'atau bahkan grafik Indonesia yang cenderung turun. Bahkan di awal tahun 2022, grafik Eropa-Amerika '
                'dengan Dunia hampir berhimpit. Salah satu faktor ini kemungkinan besar penggunaan mata uang pembelian '
                'barang-barang masih menggunakan mata uang negara di Eropa dan Amerika. ')
elif selected_option == "English":
    st.markdown("The Russian Invasion of Ukraine, which began in February 2022, has had a significant impact on "
                "the global economy. Prices have started to rise. This can be seen from the increasing inflation. "
                "The Consumer Price Index (CPI) curve in several countries has started to climb. As shown in the "
                "image below, **_there has been an increase in the CPI index in February 2022_** (indicated by the "
                "dashed line). **_Indonesia's inflation_** (blue line) **_has managed to remain_** around the"
                " inflation rates of Southeast Asia and East Asia (light blue line) since 2019, even below "
                "the global increase percentage (red line). So far, the average global inflation movement is still "
                "heavily influenced by the inflation movements of European and North American countries. This can "
                "be seen in the pattern of the rising and falling lines. In December 2019 and January 2020, all "
                "inflations increased, but the gradual slope of the global line resembles that of Europe and "
                "North America. In contrast, the slope of Southeast Asian and East Asian inflation is relatively steep "
                "or even downward, as seen in the graph of Indonesia. In early 2022, the Europe-America graph almost "
                "coincided with the global graph. One possible factor is the continued use of European and American "
                "currencies for purchasing goods.")


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

for i, item in enumerate(lp1.get_lines()):
    item.set_linewidth(line_widths1[i])
    lbl = item.get_label()
    ax1.annotate(lbl, (38, df1.loc[df1['Period'] == 'Mar-22', lbl]),
                 (41, df1.loc[df1['Period'] == 'Mar-22', lbl] + add_lbl_pos1[i]),
                 fontweight="bold", fontsize=12, color=colors1[i], va="center",
                 arrowprops={"arrowstyle": "-", "color": colors1[i]})

fig1.supxlabel('Source: Bank of Indonesia, access: 1 Oct 22 and https://ilostat.ilo.org, access: 8 Oct 22',
               x=0.3, y=0, size=10)
ax1.set_xlabel("Period", fontsize=14)
ax1.set_ylabel("Percentage (%)\n", fontsize=14)
ax1.axvline(x=37, linestyle='--', color='r')
ax1.text(36.9, 12, 'Russia\n-Ukraine War', color='r', ha='right', va='top')
ax1.get_legend().remove()
ax1.grid(True, which='both')
# plt.tight_layout(rect=(0, 0, 1, 0.90))
st.pyplot(fig1)

# ------------------------------------------------------------------------------------------------------
if selected_option == "Bahasa Indonesia":
    st.markdown('Sementara pada bulan Agustus 2022, inflasi Indonesia **_sudah mulai naik ke nilai 5 hingga 6 '
                'persen._** Kenaikan persentase inflasi CPI Indonesia sudah mulai di atas Asia Tenggara dan Timur '
                'sejak awal tahun 2022, dan terus merangkak naik, meskipun masih jauh dibawah persentase dunia. '
                'Meskipun nilai ini masih di bawah nilai Indeks Dunia, namun Indonesia harus mulai hati-hati. '
                'Kehati-hatian ini didasarkan karena besaran inflasi akan berpengaruh pada kekuatan nilai Rupiah '
                'terhadap mata uang asing terutama Dollar. Jika nilai Rupiah tertekan, maka nilai impor Indonesia '
                'terhadap mata uang asing akan naik.')
    st.markdown('Salah satu impor terbesar Indonesia yaitu impor energi/migas. Dan '
                'sektor yang mengonsumsi energi terbesar di tahun 2021 yaitu sektor transportasi, sebesar '
                '388,42 juta BOE (Barrel Oil Equivalent) atau 42,72% dari total konsumsi energi nasional *(1). '
                'Sehingga, sebagian bahan bakar minyak yang merupakan hasil impor menjadi salah satu sektor subsidi '
                'terbesar di Indonesia. Apabila Rupiah tertekan, hal ini akan sangat membebani APBN negara, karena '
                'nilai impor akan menjadi semakin mahal, karena membeli dengan menggunakan Dollar '
                'Per tanggal 12 Oktober 2022, **_nilai Rupiah terhadap Dollar sudah mencapai Rp15.300/USD._** '
                'Apabila hal ini terus bertahan, maka neraca energi APBN Indonesia akan menjadi defisit. Oleh karena '
                'itu, harus ada perubahan/perbaikan kebijakan mengenai subsidi energi ini kedepannya.')
elif selected_option == "English":
    st.markdown("Meanwhile, in August 2022, Indonesia's inflation **_has started to rise to the range of 5 to 6 "
                "percent._** The percentage increase in Indonesia's CPI inflation has been higher than that of "
                "Southeast Asia and East Asia since the beginning of 2022, and it continues to climb, although still "
                "far below the global percentage. Although this value is still below the global index, Indonesia "
                "needs to be cautious. This caution is based on the fact that the magnitude of inflation will affect "
                "the strength of the Rupiah against foreign currencies, especially the Dollar. If the value of the "
                "Rupiah is under pressure, the value of Indonesia's imports in foreign currency will increase.")
    st.markdown("One of Indonesia's largest imports is energy/oil and gas. The transportation sector was the largest "
                "energy consumer in 2021, accounting for 388.42 million BOE (Barrel Oil Equivalent) or 42.72% of "
                "the total national energy consumption *(1). Therefore, a significant portion of imported fuel "
                "becomes one of the largest subsidy sectors in Indonesia. If the Rupiah is under pressure, it will "
                "put a heavy burden on the country's state budget (APBN) because import values will become more "
                "expensive when purchasing in Dollars. As of October 12, 2022, the value of the Rupiah against "
                "the Dollar **_has reached Rp15,300/USD._** If this situation persists, Indonesia's energy balance in "
                "the state budget will be in deficit. Therefore, there needs to be changes/improvements in future "
                "energy subsidy policies.")

st.markdown("""---""")

# ------------------------------------------------------------------------------------------------------
if selected_option == "Bahasa Indonesia":
    st.markdown('# II. Energi dan Energi Terbarukan')
    st.image('renewable_energy.jpg', caption='Pengembangan Eneri Terbarukan di California Desert '
                                             'oleh mypubliclands di bawah lisensi CC BY 2.0.')
elif selected_option == "English":
    st.markdown('# II. Energy and Renewable Energy')
    st.image('renewable_energy.jpg', caption='Renewable Energy Development in the California Desert '
                                             'by mypubliclands is licensed under CC BY 2.0.')
# Tulisan 2
if selected_option == "Bahasa Indonesia":
    st.markdown("Melansir dari Handbook of Energy & Economic Statistics of Indonesia 2021, "
                "energi yang dihasilkan tahun 2021 yaitu sebesar 1,545,557,232 BOE (Barrel Oil Equivalent) "
                "atau sekitar 2626.58 Terawatt Hour. Sementara energi yang digunakan atau dikonsumsi tahun 202i "
                "yaitu sebesar 909,244,973 BOE atau sekitar 1545.21 Terawatt Hour. Hal ini menjadi hal positif "
                "untuk ketahanan energi Indonesia dimana **_Indonesia masih bisa surplus di bidang ketahanan "
                "energi._** Namun Indonesia harus tetap berhati-hati. Faktor surplus tersebut, **_kemungkinan "
                "dikarenakan tahun 2021 masih merupakan tahun perbaikan/penyesuaian akibat wabah Covid-19_**, "
                "dimana belum sepenuhnya energi dibutuhkan oleh masyarakat diantaranya masih adanya WFH di berbagai "
                "kota, sehingga kebutuhan transportasi masih rendah, dan sebagainya.")
elif selected_option == "English":
    st.markdown("According to the Handbook of Energy & Economic Statistics of Indonesia 2021, the energy produced "
                "in 2021 amounted to 1,545,557,232 BOE (Barrel Oil Equivalent) or approximately 2,626.58 "
                "Terawatt-hours. Meanwhile, the energy used or consumed in 2021 amounted to 909,244,973 BOE or "
                "approximately 1,545.21 Terawatt-hours. This is a positive aspect for Indonesia's energy resilience "
                "as **_Indonesia is still able to maintain an energy surplus._** However, Indonesia must remain "
                "cautious. The surplus factor is **_likely due to the year 2021 being a period of recovery/adjustment "
                "due to the Covid-19 pandemic_**, where energy demand has not fully returned to normal as there are "
                "still remote working arrangements in various cities, resulting in lower transportation needs, "
                "among other factors.")


# ------------------------------------------------------------------------------------------------------
# Ambil Data dan Tabel ------------> Gambar 2
df2 = pd.read_csv('primary_energy_source_bar.csv')
df2 = df2[(df2['Year'] >= 2000)]  # lebih besar dari tahun 2000
# df2_1 = df2[(df2['Entity'] == 'Indonesia')].tail(10).reset_index().drop(['index', 'Code'], axis=1)

# ------------------------------------------------------------------------------------------------------
if selected_option == "Bahasa Indonesia":
    st.markdown('Pembagian jenis energi yang digunakan oleh Indonesia dapat dilihat pada tabel di bawah ini. '
                'Dapat terlihat bahwa masih besar angka penggunaan luaran energi dari sumber daya tidak terbarukan '
                '(Non renewable). Sementara jumlah penggunaan dari sumber daya terbarukan (renewable) masih cukup '
                'sedikit. Dari surplus energi tahun lalu, ada baiknya Indonesia memulai perlahan-lahan untuk melakukan '
                'perubahan energi dari non renewable menjadi renewable energi. ')
    st.markdown('Berikut ini tabel penggunaan energi dari berbagai negara: (untuk melihat pilih negaranya dan '
                'klik update)')
elif selected_option == "English":
    st.markdown("The distribution of energy types used by Indonesia can be seen in the table below. It can be "
                "observed that a significant portion of energy usage comes from non-renewable resources. Meanwhile, "
                "the utilization of renewable resources is still relatively low. Considering the energy surplus from "
                "the previous year, it would be advisable for Indonesia to gradually initiate the transition from "
                "non-renewable to renewable energy.")
    st.markdown("Below is a table showing the energy consumption of various countries: (select the country to "
                "view and click update)")

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

if selected_option == "Bahasa Indonesia":
    st.markdown('Dari gambar di bawah ini, jika dibandingkan dengan negara lain, konsumsi energi yang '
                'digunakan oleh Indonesia (warna biru, gambar bawah) termasuk nilai yang cukup kecil. '
                'Sebagai informasi, negara dengan konsumsi batubara/coal dan minyak/oil yang terbesar yaitu '
                'Amerika Serikat menggunakan energi dari oil dan batubara masing-masing mencapai diatas 10000 '
                'dan 6000 TWh. Begitu pula untuk energi terbarukan, dimana Indonesia juga menggunakan energi '
                'yang cukup rendah jika dibandingkan dengan negara pengonsumsi '
                'renewable energy terbesar yaitu China. Perbandingan Indonesia dengan keseluruhan '
                'negara dapat dilihat pada gambar di bawah ini, dimana Indonesia ditandai dengan warna biru.')
elif selected_option == "English":
    st.markdown("From the image below, when compared to other countries, the energy consumption used by Indonesia "
                "(blue color, bottom image) is relatively small. For reference, the United States has the highest "
                "consumption of coal and oil, with energy usage from oil and coal reaching above 10,000 and 6,000 TWh "
                "respectively. The same goes for renewable energy, where Indonesia's usage is relatively low "
                "compared to the largest consumer of renewable energy, China. The comparison between Indonesia and "
                "other countries can be seen in the image below, where Indonesia is marked in blue.")

# ------------------------------------------------------------------------------------------------------
df2['Country_Code'] = 1  # untuk area scatter
df2.loc[df2.Entity == 'Indonesia', 'Country_Code'] = 30
# df2['Entity'] = df2['Entity'].astype('string')
discard2 = ["World", "High-income countries", "Non-OECD (BP)", "OECD (BP)", "Asia", "Asia Pacific (BP)",
            "Upper-middle-income countries", "North America", "North America (BP)", "Europe",
            "European Union (27)", "Lower-middle-income countries", "Middle East (BP)",
            "South and Central America (BP)", "South America", "CIS (BP)", "Africa (BP)", "Africa",
            "Other Africa (BP)"]
df2_ = df2[~df2.Entity.str.contains('|'.join(discard2))]
if selected_option == "Bahasa Indonesia":
    colors2 = {1: 'Lainnya', 30: 'Indonesia'}
elif selected_option == "English":
    colors2 = {1: 'Other', 30: 'Indonesia'}
type2 = ['Coal Consumption - TWh', 'Oil Consumption - TWh', 'Gas Consumption - TWh', 'Hydro Consumption - TWh',
         'Wind Consumption - TWh', 'Solar Consumption - TWh', 'Geo Biomass Other - TWh']
title2 = ['Coal', 'Oil', 'Gas', 'Hydro', 'Wind', 'Solar', 'Other']

if selected_option == "Bahasa Indonesia":
    def figure2(tipe2, title):
        fig = px.scatter(data_frame=df2_,
                         x='Year',
                         y=tipe2,
                         size='Country_Code',
                         color=df2_['Country_Code'].map(colors2)
                         )
        fig.update_layout(
            title={
                'text': 'Energi yang Dikonsumsi Berdasarkan Jenis Sumber Daya<br>' + title,
                'x': 0.5,
                'xanchor': 'center',
                'y': 0.95,
                'yanchor': 'top'
            },
            title_font_color="lightblue",
            xaxis_title='Tahun',
            yaxis_title="Jumlah Konsumsi - TWh",
            legend_title='Negara'
        )
        config = {'displaylogo': False,
                  'modeBarButtonsToRemove': ['zoom'],
                  'scrollZoom': True}
        fig.update_traces(hovertemplate='<br>Tahun: %{x}<br>Konsumsi: %{y} TWh')  # Negara: ' + df2_['Entity'] + '
        st.plotly_chart(fig, config=config)

    tab2_0, tab2_1, tab2_2, tab2_3, tab2_4, tab2_5, tab2_6 = st.tabs(["Batubara", "Minyak", 'Gas', 'Air',
                                                                      'Angin', 'Surya', 'Lainnya'])

elif selected_option == "English":
    def figure2(tipe2, title):
        fig = px.scatter(data_frame=df2_,
                         x='Year',
                         y=tipe2,
                         size='Country_Code',
                         color=df2_['Country_Code'].map(colors2)
                         )
        fig.update_layout(
            title={
                'text': 'Energy Consumed by Type of Resource<br>' + title,
                'x': 0.5,
                'xanchor': 'center',
                'y': 0.95,
                'yanchor': 'top'
            },
            title_font_color="lightblue",
            xaxis_title='Year',
            yaxis_title="Total Consumption - TWh",
            legend_title='Country'
        )
        config = {'displaylogo': False,
                  'modeBarButtonsToRemove': ['zoom'],
                  'scrollZoom': True}
        fig.update_traces(hovertemplate='<br>Year: %{x}<br>Consumption: %{y} TWh')  # Negara: ' + df2_['Entity'] + '
        st.plotly_chart(fig, config=config)

    tab2_0, tab2_1, tab2_2, tab2_3, tab2_4, tab2_5, tab2_6 = st.tabs(["Coal", "Oil", 'Gas', 'Water',
                                                                      'Wind', 'Solar', 'Other'])

tabs2 = [tab2_0, tab2_1, tab2_2, tab2_3, tab2_4, tab2_5, tab2_6]
for i in range(0, 7):
    with tabs2[i]:
        figure2(type2[i], title2[i])

# ------------------------------------------------------------------------------------------------------
if selected_option == "Bahasa Indonesia":
    st.markdown('Energi yang digunakan dan dikonsumsi Indonesia memang terlihat tidak besar dibandingkan negara '
                'lain dan tidak berpengaruh besar secara nilainya. Ini berpengaruh pada pengelolaan penggunaan energi '
                'di Indonesia. Namun sayangnya Indonesia merupakan negara yang belum baik dalam mengelola sumber daya '
                'energi. Hal ini tercermin pada peringkat ketahanan energi Indonesia di dunia. Pada tahun 2014, '
                'Indonesia berada pada peringkat ke-69 dari 129 negara. Meski demikian, belakangan ini peringkat '
                'Indonesia dalam ketahanan energi semakin baik. **_Pada tahun 2021, World Energy Council '
                'menetapkan Indonesia menduduki peringkat ke 56 dari 100 negara_** dalam hal ketahanan energi '
                'nasional. Hal ini menunjukkan semakin membaiknya perbaikan pengelolaan energi. Seharusnya semakin '
                'baiknya pengelolaan energi, harus diimbangi dengan perlindungan terhadap lingkungan hidup. Hal ini '
                'agar sesuai dengan Kebijakan Energi Nasional PP No. 79 Tahun 2014. Selain itu juga demi menuju '
                'transisi energi dan net zero emission di tahun 2060 *(2).')
    st.markdown('Jika melihat dari data persentase energi terbarukan Indonesia masih sangat rendah. Indonesia hampir '
                'tidak pernah di atas rata-rata dunia sejak tahun 1970. Hal ini perlu diperbaiki apabila Indonesia '
                'masih ingin mengejar net zero emission, dimana net zero emission umumnya dihasilkan oleh energi '
                'yang berasal dari Karbon, seperti batubara dan minyak.')

elif selected_option == "English":
    st.markdown("The energy used and consumed by Indonesia may appear small compared to other countries and may not "
                "have a significant impact in terms of quantity. However, this does affect the management of energy "
                "usage in Indonesia. Unfortunately, Indonesia is a country that has not been effective in managing "
                "its energy resources. This is reflected in Indonesia's energy resilience ranking in the world. "
                "In 2014, Indonesia ranked 69th out of 129 countries. Nevertheless, in recent years, Indonesia's "
                "ranking in energy resilience has improved. **_In 2021, the World Energy Council ranked Indonesia "
                "56th out of 100 countries_** in terms of national energy resilience. This indicates an improvement "
                "in energy management. However, the improvement in energy management should be accompanied by "
                "environmental protection, in line with National Energy Policy Regulation No. 79 of 2014. "
                "Additionally, this is necessary to achieve the energy transition and net-zero emissions by 2060 *(2).")
    st.markdown("Looking at the percentage of renewable energy data, Indonesia's share is still very low. Since 1970, "
                "Indonesia has rarely been above the global average in terms of renewable energy usage. This needs "
                "to be improved if Indonesia aims to pursue net-zero emissions, as net-zero emissions are generally "
                "achieved through carbon-based energy sources such as coal and oil.")

# ------------------------------------------------------------------------------------------------------
# Ambil Data dan Tabel ------------> Gambar 3
# renewable_share_energy = 'https://drive.google.com/file/d/1ZTMqQiciLIXnxJ7rni4kPHmMQKZ65QhA/view?usp=sharing'
# url3 = 'https://drive.google.com/uc?id=' + renewable_share_energy.split('/')[-2]
df3 = pd.read_csv('renewable_share_energy.csv')
df3.rename({'Renewables (% equivalent primary energy)': '%Renewable'}, axis='columns', inplace=True)
# df3_1 = df3[df3['Entity'].str.contains("Norway|Indonesia|Iceland|World|Turkey") == True]
choose3 = ["Norway", "Indonesia", "Iceland", "World", "Turkey"]
df3_ = df3[df3.Entity.str.contains('|'.join(choose3))]

fig3, ax3 = plt.subplots(1, 1, figsize=(14, 7))
colors3 = ["tab:pink", "darkblue", "tab:cyan", "tab:gray", "tab:red"]
df3_.groupby(['Year', 'Entity'])['%Renewable'].sum().unstack().plot(kind='line', ax=ax3, marker='.', color=colors3)
df3_1_country = df3_['Entity'].unique()
x1 = [2020, 2020, 2020, 2020, 2021]
y1 = [86, 10, 71, 19, 13]
x2 = [2020, 2020, 2020, 2020, 2023]
y2 = [93, 1, 65, 24, 11]
for i, anno in enumerate(df3_1_country):
    ax3.annotate(df3_1_country[i], xy=(x1[i], y1[i]), xytext=(x2[i], y2[i]),
                 fontweight="bold", fontsize=12, color=colors3[i],
                 va="center", arrowprops={"arrowstyle": "-", "color": colors3[i]})
if selected_option == "Bahasa Indonesia":
    plt.title('Besaran Persentase Penggunaan Energi Terbarukan', loc='center', pad=30, fontsize=20, color='blue')
    ax3.set_xlabel('Tahun', fontsize=13.5)
    ax3.set_ylabel('Konsumsi Energi Terbarukan/\nKonsumsi Seluruh Energi (%)\n', fontsize=13.5)
    fig3.supxlabel('Sumber: https://ourworldindata.org/energy, akses: 24 Sep 22', x=0.26, y=0.02, size=12)
elif selected_option == "English":
    plt.title('The Percentage of Renewable Energy Use', loc='center', pad=30, fontsize=20, color='blue')
    ax3.set_xlabel('Year', fontsize=13.5)
    ax3.set_ylabel('Renewable Energy Consumption/\nAll Energy Consumption (%)\n', fontsize=13.5)
    fig3.supxlabel('Source: https://ourworldindata.org/energy, access: 24 Sep 22', x=0.26, y=0.02, size=12)
# ax3.legend(loc='upper right', bbox_to_anchor=(1.1, 1), shadow=True, ncol=1)
ax3.get_legend().remove()
st.pyplot(fig3)

# ------------------------------------------------------------------------------------------------------
if selected_option == "Bahasa Indonesia":
    st.markdown('Indonesia cukup jauh tertinggal dibandingkan **_negara-negara Skandinavia_**, dimana rata-rata negara '
                'tersebut sudah **_memiliki sumber renewable energy di atas 50 persen_**. Bahkan negara yang memiliki '
                'GDP setingkat Indonesia, Turki sudah memiliki persentase renewable energi di atas Indonesia. '
                'Hal ini mungkin disebabkan oleh fokus Turki melalui Eleventh Development Plan (2019-2023) untuk '
                'dapat menghasilkan/ menggunakan energi terbarukan sebesar 38.8% *(3). ')
    st.markdown('Namun Indonesia (grafik warna biru) sudah mulai bergerak menanjak ke atas sejak tahun 2014. '
                'Hal ini salah satunya merupakan dampak dari Kebijakan Energi Nasional yang telah dimulai pada tahun '
                'yang sama. Meskipun sudah mulai naik nilai persentase penggunaan energi terbarukan, namun masih perlu '
                'lebih banyak investasi dan pergerakan uang untuk energi terbarukan. Grafik di bawah ini menunjukkan '
                'besaran capital yang berhubungan dengan sumber energi renewable, baik investasi ataupun pergerakan '
                'nilai uang yang berhubungan dengan Renewable Energy. Kita akan membandingkan dengan negara Brazil '
                'karena negara tersebut sedang menginvestasikan pada energi terbarukan dengan nilai cukup besar.')
elif selected_option == "English":
    st.markdown("Indonesia lags behind **_Scandinavian countries_**, where on average these countries already have "
                "**_over 50 percent renewable energy sources_**. Even countries with a similar GDP to Indonesia, "
                "such as Turkey, have a higher percentage of renewable energy than Indonesia. This may be due to "
                "Turkey's focus through the Eleventh Development Plan (2019-2023) to achieve a renewable energy "
                "share of 38.8% *(3).")
    st.markdown("However, Indonesia (blue line on the graph) has been gradually increasing since 2014. This is "
                "partly due to the implementation of the National Energy Policy that started in the same year. "
                "Although the percentage of renewable energy usage has started to increase, there is still a need "
                "for more investment and financial movement towards renewable energy. The graph below shows the "
                "capital associated with renewable energy, including investments and financial transactions. We will "
                "compare it with Brazil because Brazil is currently making significant investments in renewable "
                "energy.")

# ------------------------------------------------------------------------------------------------------
# Ambil Data dan Tabel ------------> Gambar 4
# table_invest_final = 'https://drive.google.com/file/d/1ZTMqQiciLIXnxJ7rni4kPHmMQKZ65QhA/view?usp=sharing'
# url4 = 'https://drive.google.com/uc?id=' + table_invest_final.split('/')[-2]
df4 = pd.read_csv('table_invest_final.csv')
df4.rename({'Country/area': 'Country', 'Public Flows (2020 USD M)': 'Public Flows'}, axis='columns', inplace=True)
df4['Country_Code'] = 3  # untuk luas scatter
df4.loc[df4.Country == 'Brazil', 'Country_Code'] = 30  # untuk luas scatter
df4.loc[df4.Country == 'Indonesia', 'Country_Code'] = 35  # untuk luas scatter
if selected_option == "Bahasa Indonesia":
    colors4 = {3: 'Lainnya', 30: 'Brazil', 35: 'Indonesia'}
elif selected_option == "English":
    colors4 = {3: 'Other', 30: 'Brazil', 35: 'Indonesia'}
tech4 = ['Solar photovoltaic', 'Onshore wind energy', 'Renewable hydropower', 'Geothermal energy',
         'Renewable municipal waste', 'Multiple renewables']

if selected_option == "Bahasa Indonesia":
    def figure4(tech):
        # fig, axs = plt.subplots(1, 1, figsize=(7, 4))
        fig = px.scatter(data_frame=df4.loc[df4['Technology'] == tech],
                         x='Year',
                         y='Public Flows',
                         size='Country_Code',
                         color=df4.loc[df4['Technology'] == tech, ['Country_Code']].squeeze().map(colors4))
        fig.update_layout(
            title={
                'text': 'Besaran Pergerakan Capital Energi Terbarukan',
                'x': 0.5,
                'xanchor': 'center',
                'y': 0.95,
                'yanchor': 'top'},
            title_font_color="lightblue",
            xaxis_title='Tahun',
            yaxis_title="Nilai Capital Public Flows<br>(USD Juta)",
            legend_title='Negara'
        )
        config = {'displaylogo': False,
                  'modeBarButtonsToRemove': ['zoom'],
                  'scrollZoom': True}
        fig.update_traces(hovertemplate='Tahun: %{x}<br>Nilai Public Flow: USD %{y} juta')
        st.plotly_chart(fig, config=config)

    tab4_0, tab4_1, tab4_2, tab4_3, tab4_4, tab4_5 = st.tabs(["Energi Surya", "Energi Angin",
                                                              'Energi Air', 'Energi Geothermal',
                                                              'Energi Limbah', 'Lainnya'])

elif selected_option == "English":
    def figure4(tech):
        # fig, axs = plt.subplots(1, 1, figsize=(7, 4))
        fig = px.scatter(data_frame=df4.loc[df4['Technology'] == tech],
                         x='Year',
                         y='Public Flows',
                         size='Country_Code',
                         color=df4.loc[df4['Technology'] == tech, ['Country_Code']].squeeze().map(colors4))
        fig.update_layout(
            title={
                'text': 'Renewable Energy Capital Movement Amount',
                'x': 0.5,
                'xanchor': 'center',
                'y': 0.95,
                'yanchor': 'top'},
            title_font_color="lightblue",
            xaxis_title='Year',
            yaxis_title="Value of Capital Public Flows<br>(USD Mil.)",
            legend_title='Country'
        )
        config = {'displaylogo': False,
                  'modeBarButtonsToRemove': ['zoom'],
                  'scrollZoom': True}
        fig.update_traces(hovertemplate='Year: %{x}<br>Nilai Public Flow: USD %{y} million')
        st.plotly_chart(fig, config=config)

    tab4_0, tab4_1, tab4_2, tab4_3, tab4_4, tab4_5 = st.tabs(["Solar Energy", "Wind Energy",
                                                              'Water Energy', 'Geothermal Energy',
                                                              'Waste Energy', 'Other'])

tabs4 = [tab4_0, tab4_1, tab4_2, tab4_3, tab4_4, tab4_5]
for i in range(0, 6):
    with tabs4[i]:
        figure4(tech4[i])

if selected_option == "Bahasa Indonesia":
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
                '(atau mungkin belum terdata). Sementara beberapa negara sudah mulai menggunakan energi dari '
                'pembuangan limbah, seperti Finlandia dan Perancis. Kedepannya dimana produksi limbah Indonesia yang '
                'cukup besar, diharapkan Indonesia mampu menggunakan teknologi dengan memanfaatkan energi yang '
                'dihasilkan dari limbah tersebut.')
elif selected_option == "English":
    st.markdown("When compared to Brazil, one of the countries that is serious about developing renewable energy, "
                "Indonesia is still behind Brazil in terms of public flow for renewable energy. There could be "
                "several possible reasons. First, Brazil's higher GDP compared to Indonesia. Second, the extensive "
                "resources that can be utilized, such as hydropower in the Amazon River or wind energy along the "
                "coastline. However, Indonesia should also be capable of implementing similar measures. Indonesia "
                "has a long coastline of approximately 95,181 km, which can be utilized for harnessing offshore wind "
                "power, and it also has significant river systems. Nonetheless, at present, Indonesia is focusing "
                "more on geothermal energy utilization, as seen in the geothermal section of the graph.")
    st.markdown("Indonesia itself is currently focusing on geothermal energy. This is evident from the financial "
                "movement associated with this energy type. Additionally, the use of energy from waste is not yet "
                "apparent (or perhaps not yet recorded). Meanwhile, some countries have started utilizing energy "
                "from waste, such as Finland and France. In the future, considering Indonesia's substantial waste "
                "production, it is expected that Indonesia will be able to leverage technology to harness energy "
                "generated from waste.")

# ------------------------------------------------------------------------------------------------------
if selected_option == "Bahasa Indonesia":
    st.subheader('Penutup')
    st.markdown('Dari data-data yang telah dipaparkan di atas, ada beberapa kesimpulan yang dapat diambil berkaitan '
                'energi terbarukan. Pertama, penggunaan energi tidak terbarukan dapat mulai dikurangi. Hal ini dapat '
                'meringankan nilai impor Indonesia terhadap asing. Kedua, investasi untuk beberapa area pembangkit '
                'dapat ditingkatkan, seperti pembangkit energi tenaga surya, dan energi pembangkit tenaga angin. '
                'Selain itu, sumber energi dari limbah mulai dapat diekplorasi karena cukup banyaknya limbah '
                'Indonesia. Oleh karena itu, kedepannya diharapkan Indonesia mampu mencapai tantangan zero emission '
                'di tahun 2060. Komitmen dan peran serta pemerintah dan masyarakatlah yang mampu menjawab tantangan '
                'tersebut.')
elif selected_option == "English":
    st.subheader('Conclusion')
    st.markdown("Based on the data presented above, several conclusions can be drawn regarding renewable energy. "
                "First, the use of non-renewable energy can be reduced, which can help alleviate Indonesia's "
                "dependence on foreign imports. Second, investments in certain power generation areas, such as "
                "solar and wind energy, can be increased. Additionally, the utilization of energy from waste can "
                "be explored due to the substantial amount of waste in Indonesia. Therefore, it is hoped that "
                "Indonesia will be able to achieve the challenge of zero emissions by 2060. The commitment and "
                "participation of the government and society are crucial in addressing this challenge.")

# ------------------------------------------------------------------------------------------------------
st.markdown("""---""")
if selected_option == "Bahasa Indonesia":
    'Referensi :'
    st.markdown('1. https://www.esdm.go.id/assets/media/content/content-handbook-of-energy-and-economic-statistics-of-'
                'indonesia-2021.pdf, akses: 13 Oktober 2022.')
    '2. https://suarakarya.co.id/indonesia-duduki-peringkat-ke-56-ketahanan-energi/35469/, akses: 13 Oktober 2022.'
    '3. https://www.iea.org/reports/turkey-2021, akses: 14 Oktober 2022.'
elif selected_option == "English":
    'Reference :'
    st.markdown('1. https://www.esdm.go.id/assets/media/content/content-handbook-of-energy-and-economic-statistics-of-'
                'indonesia-2021.pdf, access: 13 Oktober 2022.')
    '2. https://suarakarya.co.id/indonesia-duduki-peringkat-ke-56-ketahanan-energi/35469/, access: 13 Oktober 2022.'
    '3. https://www.iea.org/reports/turkey-2021, access: 14 Oktober 2022.'
