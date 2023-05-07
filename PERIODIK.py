import streamlit as st 
from streamlit_option_menu import option_menu

navbar= option_menu(menu_title=None, options= ["Home","Periodik Unsur", 'Simbol Bahaya dan Bahan Kimia'], default_index=0, icons=['house-door','book','exclamation-diamond'])

if navbar== "Home":
    st.title ("PROJECT TUGAS AKHIR LPK KELOMPOK 1")
    st.write ('''
    Selamat datang di aplikasi kami!!!\n
    Aplikasi ini diharapkan dapat bermanfaat bagi penggunanya\n
    ''')
    st.write ('''Anggota Kelompok:\n
    Gita Ayu Larassati (2219077)\n
    Kalyana Tantri Eka T.A (2219090)\n
    Mei Dwi Puput K.M (2219107)\n
    Naufal Nabil (2219127)\n
    ''')

if navbar=='Periodik Unsur':
    periode= st.selectbox('periode unsur',options=['pilih periode','periode 1','periode 2','periode 3','periode 4','periode 5','periode 6','periode 7'],index=0)
    if periode=='periode 1':
        atom= st.text_input ('Masukkan Nomor Atom atau Nama Unsur')
        output= ''
        if st.button('submit'):
            if atom=='1' or atom.lower() == 'hidrogen':
                output='''
                Nomor atom= 1\n
                Golongan= I-A\n
                Nama atom= Hidrogen (H)\n
                Nama latin= Hydrogenium\n
                Nama inggris= Hydrogen\n
                Penemu= Henry Cavendish\n
                Proton= 1, Elektron= 1, Neutron= 0\n
                Berat atom= 1.00784 (g/mol)\n
                Fase= gas\n
                Perkiraan ion= H+,H-\n
                Valensi= I'''
            elif atom=='2' or atom.lower() == 'helium':
                output='''
                Nomor atom= 2\n
                Golongan= VIII-A\n
                Nama atom= Helium (He)\n
                Nama latin= Helium\n
                Nama inggris= Helium\n 
                Penemu= Pierre Jules César Janssen, Joseph Norman Lockyer\n
                Proton= 2, Elektron= 2, Neutron= 2\n
                Berat atom= 10.811 (g/mol)\n
                Fase= Solid\n
                Perkiraan ion= -\n
                Valensi= 0'''
            else:
                st.error('nomor tersebut tidak terdapat di periode ini silahkan input yang lain!')
        st.write (output)

    if periode=='periode 2':
        atom= st.text_input ('masukkan nomor atom atau nama unsur')
        output= ''
        if st.button('submit'):
            if atom=='3' or atom.lower() == 'litium':
                output='''
                Nomor atom= 3\n
                Golongan= I-A\n
                Nama atom= Li (Litium)\n
                Nama latin= Lithium\n
                Nama inggris= Lithium\n
                Penemu= Johan August Arfwedson\n
                Proton= 3, Elektron= 3, Neutron= 4\n
                Berat atom= 6.941 (g/mol)\n
                Fase= solid\n
                Perkiraan ion= Li⁺\n 
                Valensi= 1'''
            elif atom=='4' or atom.lower() == 'berilium':
                output='''
                Nomor atom= 4\n
                Golongan= II-A\n
                Nama atom= Berilium (Be)\n
                Nama latin= Berylium\n
                Nama inggris= Berylium\n
                Penemu= Louis-Nicolas Vauquelin\n
                Proton= 4, Elektron= 4, Neutron= 5\n
                Berat atom= 9.0121 (g/mol)\n
                Fase= Solid\n
                Perkiraan ion= Be2+\n
                Valensi= 2'''
            elif atom=='5' or atom.lower() == 'boron':
                output=''' 
                Nomor atom= 5\n
                Golongan= III-A\n
                Nama atom= Boron (B)\n
                Nama latin= Borum\n
                Nama inggris= Boron\n
                Penemu= Joseph-Louis Gay-Lussac, Louis Jacques Thénard, Humphry Davy\n
                Proton= 5, Elektron= 5, Neutron= 6\n
                Berat atom= 10.811 (g/mol)\n
                Fase= Solid\n
                Perkiraan ion= -\n
                Valensi= 3'''
            elif atom=='6' or atom.lower() == 'karbon':
                output='''
                Nomor atom= 6\n
                Golongan= IV-A\n
                Nama atom= C (Karbon)\n
                Nama latin= Carbonium\n
                Nama inggris= Carbon\n
                Penemu= Antoine Laurent de Lavoisier\n
                Proton= 6, Elektron= 6, Neutron= 6\n
                Berat atom= 12.0107 (g/mol)\n
                Fase= Solid\n
                Perkiraan ion= -\n
                Valensi= 2,4'''
            elif atom=='7' or atom.lower() == 'nitrogen':
                output='''
                Nomor atom= 7\n
                Golongan= V-A\n
                Nama atom= N (Nitrogen)\n
                Nama latin= Nitrogenium\n
                Nama inggris= Nitrogen\n
                Penemu= Daniel Rutherford\n
                Proton= 7, Elektron= 7, Neutron= 7\n
                Berat atom= 14.0067 (g/mol)\n
                Fase= Gas\n
                Perkiraan ion= N3-\n
                Valensi= 3'''
            elif atom=='8' or atom.lower() == 'oksigen':
                output='''
                Nomor atom= 8\n
                Golongan= VI-A\n
                Nama atom= O (Oksigen)\n
                Nama latin= Oxygeniun\n
                Nama inggris= Oxygen\n
                Penemu= Michał Sędziwó, Joseph Priestley, Carl Wilhelm Scheele\n
                Proton= 8, Elektron= 8, Neutron= 8\n
                Berat atom= 15.9994 (g/mol)\n
                Fase= Gas\n
                Perkiraan ion= O2-\n
                Valensi= 2'''
            elif atom=='9' or atom.lower() == 'fluor':
                output='''
                Nomor atom= 9\n
                Golongan= VII-A\n
                Nama atom= F (Fluor)\n
                Nama latin= Fluorum\n
                Nama inggris= Fluorine\n
                Penemu= Ferdinand Frederic Henri Moissan\n
                Proton= 9, Elektron= 9, Neutron= 10\n
                Berat atom= 18.9984 (g/mol)\n
                Fase= Gas\n
                Perkiraan ion= F-\n
                Valensi= 1,2'''
            elif atom=='10' or atom.lower() == 'neon':
                output='''
                Nomor atom= 10\n
                Golongan= VIII-A\n
                Nama atom= Ne (Neon)\n
                Nama latin= Neon\n
                Nama inggris= Neon\n
                Penemu= Sir William Ramsay, Morris William Travers\n
                Proton= 10, Elektron= 10, Neutron= 10\n
                Berat atom= 20.1797 (g/mol)\n
                Fase= Gas\n
                Perkiraan ion= -\n
                Valensi= 0'''
            else:
                st.error('nama dan nomor atom tidak terdapat di periode ini silahkan input yang lain!')
        st.write (output)
            
    if periode=='periode 3':
        atom= st.text_input ('masukkan nomor atom atau nama unsur')
        output=''
        if st.button('submit'):
            if atom=='11' or atom.lower() == 'natrium':
                output='''
                Nomor atom= 11\n
                Golongan= I-A\n
                Nama atom : Natrium (Na)\n
                Nama latin :  Natrium\n
                Nama Inggris : Sodium\n
                Penemu : Humphry\n
                Elektron : 11, Proton : 11, Neutron : 12\n
                Berat atom : 22.9897 (g/mol)\n
                Fase : padat\n
                Perkiraan ion : Na+\n
                Valensi : I'''
            elif atom=='12' or atom.lower() == 'magnesium':
                output='''
                Nomor atom= 12\n
                Golongan= II=A\n
                Nama atom : Magnesium (Mg)\n
                Nama latin :  Magnesium \n
                Nama Inggris : Magnesium \n
                Penemu : Joseph Black, Humphry Davy\n
                Elektron : 12, Proton : 12, Neutron : 12\n
                Berat atom :24.3050  (g/mol)\n
                Fase : padat\n
                Perkiraan ion : Mg2+\n
                Valensi : II'''
            elif atom=='13' or atom.lower() == 'alumunium':
                output='''
                Nomor atom= 13\n
                Golongan= III-A\n
                Nama atom : Alumunium (Al)\n
                Nama latin :  Aluminium\n
                Nama Inggris : Aluminum\n
                Penemu : Hans Christian Orsted\n
                Elektron : 13, Proton : 13, Neutron : 14\n
                Berat atom : 26.9815 (g/mol)\n
                Fase : padat\n
                Perkiraan ion : Al3+\n
                Valensi : III'''
            elif atom=='14' or atom.lower() == 'silikon':
                output='''
                Nomor atom= 14\n
                Golongan= IV-A\n
                Nama atom : Silikon (Si)\n
                Nama latin :  Silicium\n
                Nama Inggris : Silicon\n
                Penemu : Jons Jakob Berzelius\n
                Elektron : 14, Proton : 14, Neutron : 14\n
                Berat atom : 28.0855 (g/mol)\n
                Fase : padat\n
                Perkiraan ion : -\n
                Valensi : II, IV'''
            elif atom=='15' or atom.lower() == 'fosfor':
                output='''
                Nomor atom= 15\n
                Golongan= V-A\n
                Nama atom : Fosfor (P)\n
                Nama latin :  Phosphorus\n
                Nama Inggris : Phosphorus\n
                Penemu : Hennig Brand\n
                Elektron : 15, Proton : 15, Neutron : 16\n
                Berat atom : 30.9737 (g/mol)\n
                Fase : padat\n
                Perkiraan ion : P3-\n
                Valensi : III, V'''
            elif atom=='16' or atom.lower() == 'belerang':
                output='''
                Nomor atom= 16\n
                Golongan= VI-A\n
                Nama atom : Belerang (S)\n
                Nama latin :  Sulphuris\n
                Nama Inggris : Sulfur\n
                Penemu : -\n
                Elektron : 16, Proton : 16, Neutron : 16\n
                Berat atom : 32.065 (g/mol)\n
                Fase : padat\n
                Perkiraan ion : S2-\n
                Valensi : II, IV, VI'''
            elif atom=='17' or atom.lower() == 'klor':
                output='''
                Nomor atom= 17\n
                Golongan= VII-A\n
                Nama atom : Klor (Cl)\n
                Nama latin :  Chlorum\n
                Nama Inggris : Chlorine\n
                Penemu : Carl Wilhelm Scheele\n
                Elektron : 17, Proton : 17, Neutron : 18\n
                Berat atom : 35.453 (g/mol)\n
                Fase : Gas\n
                Perkiraan ion : Cl-\n
                Valensi : I, III, V, VII'''
            elif atom=='18' or atom.lower() == 'argon':
                output='''
                Nomor atom= 18\n
                Golongan= VIII-A\n
                Nama atom : Argon (Ar)\n
                Nama latin :  Argon\n
                Nama Inggris : Argon\n
                Penemu : Sir William Ramsay\n
                Elektron : 18, Proton : 18, Neutron : 22\n
                Berat atom :39.948 (g/mol)\n
                Fase : Gas\n
                Perkiraan ion : 3\n
                Valensi : -'''
            else:
                st.error('nama dan nomor atom tidak terdapat di periode ini silahkan input yang lain!')
        st.write (output)
     
    if periode=='periode 4':
        atom= st.text_input ('masukkan nomor atom atau nama unsur')
        output=''
        if st.button('submit'):
            if atom=='19' or atom.lower() == 'kalium':
                output='''
                Nomor atom= 19\n
                Golongan= II=A\n
                Golongan= I-A\n
                Nama atom=kalium (K)\n
                Nama latin=Kalium\n
                Nama inggris=Pottasium\n
                Penemu=Humphry Davy\n
                Proton=19, Elektron=19, Neutron=20\n
                Berat atom=39.0983(g/cm³)\n
                Fase=padat\n
                Perkiraan ion=k+\n
                Valensi=I'''
            elif atom=='20' or atom.lower() == 'kalsium':
                output='''
                Nomor atom= 20\n
                Golongan= II-A\n
                Nama atom=kalsium(Ca)\n
                Nama latin=calsium\n
                Nama inggris=calcium\n
                Penemu=Humphry Davy\n
                Proton=20, Elektron=20, Neutron=20\n
                Berat atom=40.078(g/mol)\n
                Fase=padat\n
                Perkiraan ion=ca²+\n
                Valensi=II'''
            elif atom=='21' or atom.lower() == 'skandium':
                output='''
                Nomor atom= 21\n
                Golongan= III-B\n
                Nama atom=skandium(Sc)\n
                Nama latin=Scandium\n
                Nama inggris=Scandium\n
                Penemu=Lars fredrik Nilson\n
                Proton=21, Elektron=21, Neutron=24\n
                Berat atom=44.9559(g/mol)\n
                Fase=padat\n
                Perkiraan ion=Sc³+\n
                Valensi=III'''
            elif atom=='22' or atom.lower() == 'titanium':
                output='''
                Nomor atom= 22\n
                Golongan= IV-B\n
                Nama atom=Titanium (Ti)\n
                Nama latin=Titanium\n
                Nama inggris=Titanium\n
                Penemu=william\n
                Proton=22, Elektron=22, Neutron=26\n
                Berat atom=47.867(g/mol)\n
                Fase=padat\n
                Perkiraan ion=Ti⁴+,Ti³+\n
                Valensi=II,III,IV'''
            elif atom=='23' or atom.lower() == 'vanadium':
                output='''
                Nomor atom= 23\n
                Golongan= V-B\n
                Nama atom=Vanadium (V)\n
                Nama latin=Vanadium\n
                Nama inggris=Vanadium\n
                Penemu=Andres Manuel del Rio\n
                Proton=23, Elektron=23, Neutron=28\n
                Berat atom=50.9415(g/mol)\n
                Fase=padat\n
                Perkiraan ion=V³+,V⁵+\n
                Valensi=II,III,IV,V'''
            elif atom=='24' or atom.lower() == 'krom':
                output='''
                Nomor atom= 24\n
                Golongan= VI-B\n
                Nama atom=Krom (Cr)\n
                Nama latin=Chromium\n
                Nama inggris=Chromium\n
                Penemu=Louis-Nicolas Vauquelin\n
                Proton=24, Elektron=24, Neutron=28\n
                Berat atom=51.9951(g/mol)\n
                Fase=padat\n
                Perkiraan ion=Cr³+,Cr²+\n
                Valensi=II,III,VI'''
            elif atom=='25' or atom.lower() == 'mangan':
                output='''
                Nomor atom= 25\n
                Golongan= VII-B\n
                Nama atom=Mangan (Mn)\n
                Nama latin=Manganum\n
                Nama inggris=Manganese\n
                Penemu=Johan Gottileb Gahn, lgnatius Gottfried kaim\n
                Proton=25, Elektron=25, Neutron=30\n
                Berat atom=54.9830(g/mol)\n
                Fase=padat\n
                Perkiraan ion=Mn²+,Mn⁴+\n
                Valensi=II,III,IV,VI,VII'''
            elif atom=='26' or atom.lower() == 'besi':
                output='''
                Nomor atom= 26\n
                Golongan= VIII-B\n
                Nama atom=Besi (Fe)\n
                Nama latin=Ferrum\n
                Nama inggris=lron\n
                Penemu=-\n
                Proton=26, Elektron=26, Neutron=30\n
                Berat atom=55.485(g/mol)\n
                Fase=padat\n
                Perkiraan ion=Fe³+,Fe²+\n
                Valensi=II,III,VI'''
            elif atom=='27' or atom.lower() == 'kobalt':
                output='''
                Nomor atom= 27\n
                Golongan= VIII-B\n
                Nama atom=kobalt (Co)\n
                Nama latin=Cobaltium\n
                Nama inggris=Cobalt\n
                Penemu=Georg Brandt\n
                Proton=27, Elektron=27, Neutron=32\n
                Berat atom=58.9331(g/mol)\n
                Fase=padat\n
                Perkiraan ion=Co²+,Co³+\n
                Valensi=II,III'''
            elif atom=='28' or atom.lower() == 'nikel':
                output='''
                Nomor atom= 28\n
                Golongan= VIII-B\n
                Nama atom=Nikel (Ni)\n
                Nama latin=Niccolum\n
                Nama inggris=Nickel\n
                Penemu=Axel Frederic von Cronstedt\n
                Proton=28, Elektron=28, Neutron=31\n
                Berat atom=58.6934(g/mol)\n
                Fase=padat\n
                Perkiraan ion=Ni²+,Ni³+\n
                Valensi=II,III'''
            elif atom=='29' or atom.lower() == 'tembga':
                output='''
                Nomor atom= 29\n
                Golongan= I-B\n
                Nama atom=Tembaga(Cu)\n
                Nama latin=Cuprum\n
                Nama inggris=Copper\n
                Penemu=-\n
                Proton=29, Elektron=29, Neutron=35\n
                Berat atom=63,546(g/mol)\n
                Fase=padat\n 
                Perkiraan ion=cu²+,cu+\n
                Valensi=I,II'''
            elif atom=='30' or atom.lower() == 'seng':
                output='''
                Nomor atom= 30\n
                Golongan= II-B\n
                Nama atom=seng(zn)\n
                Nama latin=Zincum\n
                Nama inggris=Zinc\n
                Penemu=Andreas sigismund marggraf\n
                Proton=30, Elektron=30, Neutron=35\n
                Berat atom=65.38(g/mol)\n
                Fase=padat\n
                Perkiraan ion=Zn²+\n
                Valensi=II'''
            elif atom=='31' or atom.lower() == 'galium':
                output='''
                Nomor atom= 31\n
                Golongan= III-A\n
                Nama atom : Galium (Ga)\n
                Nama latin :  Gallium\n
                Nama Inggris : Gallium\n
                Penemu : Paul Emile Lecoq de Boisbaudran\n
                Elektron : 31, Proton : 31, Neutron : 39\n
                Berat atom : 69.723 (g/mol)\n
                Fase : padat\n
                Perkiraan ion : Ga3+\n
                Valensi : III'''
            elif atom=='32' or atom.lower() == 'germanium':
                output='''
                Nomor atom=32\n
                Golongan= IV-A\n
                Nama atom : Germanium (Ge)\n
                Nama latin :  Germanium\n
                Nama Inggris : Germanium\n
                Penemu : Clemens Alexander Winkler\n
                Elektron : 32, Proton : 32, Neutron : 41\n
                Berat atom : 72.64 (g/mol)\n
                Fase : padat\n
                Perkiraan ion : Ge4+\n
                Valensi : III, IV'''
            elif atom=='33' or atom.lower() == 'arsen':
                output='''
                Nomor atom= 33\n
                Golongan= V-A\n
                Nama atom : Arsen (As)\n
                Nama latin :  Arsenicum\n
                Nama Inggris : Arsenic\n
                Penemu : Albertus Magnus\n
                Elektron : 33, Proton : 33,Neutron : 42\n
                Berat atom :  74.9216 (g/mol)\n
                Fase : padat\n
                Perkiraan ion : As3-\n
                Valensi : III, V'''
            elif atom=='34' or atom.lower() == 'selenium':
                output='''
                Nomor atom= 34\n
                Golongan= VI-A\n
                Nama atom : Selenium (Se)\n
                Nama latin :  selenium\n
                Nama Inggris : selenium\n
                Penemu : Jons Jakob berzelius\n
                Elektron : 34, Proton : 34, Neutron : 45\n
                Berat atom :  78.96 (g/mol)\n
                Fase : padat\n
                Perkiraan ion : Se2-\n
                Valensi : II, IV, VI'''
            elif atom=='35' or atom.lower() == 'brom':
                output='''
                Nomor atom= 35\n
                Golongan= VII-A\n
                Nama atom : Brom (Br)\n
                Nama latin :  Bromum\n
                Nama Inggris : Bromine\n
                Penemu : Antoine-jerome Balard, Karl Jakob Leuwich\n
                Elektron : 35, Proton : 35, Neutron : 45\n
                Berat atom : 79.904 (g/mol)\n
                Fase : Cair\n
                Perkiraan ion : Br-\n
                Valensi : I, III, V, VII'''
            elif atom=='36' or atom.lower() == 'kripton':
                output='''
                Nomor atom= 36\n
                Golongan= VIII-A\n
                Nama atom : Kripton (Kr)\n
                Nama latin :  Krypton\n
                Nama Inggris : krypton\n
                Penemu : Sir William Ramsay, Morris William Travers\n
                Elektron : 36, Proton : 36, Neutron : 48\n
                Berat atom : 83.798 (g/mol)\n
                Fase : Gas\n
                Perkiraan ion : -\n
                Valensi : 0'''
            else:
                st.error('nama dan nomor atom tidak terdapat di periode ini silahkan input yang lain!')
        st.write (output)

    if periode=='periode 5':
        atom= st.text_input ('masukkan nomor atom atau nama unsur')
        output=''
        if st.button('submit'):
            if atom=='37' or atom.lower() == 'rubidium':
                output='''
                Nomor atom= 37\n
                Golongan= I-A\n
                Nama atom : Rubidium (Rb)\n
                Nama latin :  Rubidium\n
                Nama Inggris : Rubidium\n
                Penemu : Robert Wilhelm busen, Gustav Robert Kirchhoff\n
                Elektron : 37, Proton : 37, Neutron : 48\n
                Berat atom : 85.467 (g/mol)\n
                Fase : padat\n
                Perkiraan ion : Rb+\n
                Valensi : I'''
            elif atom=='38' or atom.lower() == 'strontium':
                output='''
                Nomor atom= 38\n
                Golongan= II=A\n
                Nama atom : Strontium (Sr)\n
                Nama latin :  Strontium\n
                Nama Inggris : Strontium\n
                Penemu : Adair Crawford\n
                Elektron : 38, Proton : 38, Neutron : 50\n
                Berat atom : 87.62 (g/mol)\n
                Fase : padat\n
                Perkiraan ion : Sr2+\n
                Valensi : II'''
            elif atom=='39' or atom.lower() == 'itrium':
                output='''
                Nomor atom= 39\n
                Golongan= III-B\n
                Nama atom : Itrium (Y)\n
                Nama latin :  Yttrium\n
                Nama Inggris : Yttrium\n
                Penemu : Johan Gadolin\n
                Elektron : 39, Proton : 39, Neutron : 50\n
                Berat atom : 88.905 (g/mol)\n
                Fase : padat\n
                Perkiraan ion : Y3+\n
                Valensi : II, III'''
            elif atom=='40' or atom.lower() == 'zirkonium':
                output='''
                Nomor atom= 40\n
                Golongan= IV-B\n
                Nama atom : Zirkonium (Zr)\n
                Nama latin :  Zirconium\n
                Nama Inggris : Zirconium\n
                Penemu : Martin Heinrich Klaproth\n
                Elektron : 40, Proton : 40, Neutron : 51\n
                Berat atom : 91.224 (g/mol)\n
                Fase : padat\n
                Perkiraan ion : Zr4+\n
                Valensi : II, III, IV'''
            elif atom=='41' or atom.lower() == 'zirkonium':
                output='''
                Nomor atom= 41\n
                Golongan= V-B\n
                Nama atom : Niobium (Nb)\n
                Nama latin :  Niobium\n
                Nama Inggris : Niobium\n
                Penemu : Charles Hatchett\n
                Elektron : 41, Proton : 41, Neutron : 52\n
                Berat atom : 92.906 (g/mol)\n
                Fase : padat\n
                Perkiraan ion : Nb5+, Nb3+\n
                Valensi : II, III, IV, V'''
            elif atom=='42' or atom.lower() == 'molibden':
                output='''
                Nomor atom= 42\n
                Golongan= VI-B\n
                Nama atom : Molibden (Mo)\n
                Nama latin :  Molybdaenum\n
                Nama Inggris : Molybdenum\n
                Penemu : Carl Wilhelm Scheele\n
                Elektron : 42, Proton : 42, Neutron : 54\n
                Berat atom :95.94 (g/mol)\n
                Fase : padat\n
                Perkiraan ion : Mo6+\n
                Valensi : IV, VI'''
            elif atom=='43' or atom.lower() == 'teknetium':
                output='''
                Nomor atom= 43\n
                Golongan= VII-B\n
                Nama atom : Teknetium (Tc)\n
                Nama latin :  Technetium\n
                Nama Inggris : Technetium\n
                Penemu : Emillio Gino Segre\n
                Elektron : 43, Proton : 43, Neutron : 55\n
                Berat atom : 98.906 (g/mol)\n
                Fase : padat\n
                Perkiraan ion : Tc7+\n
                Valensi : I, II, III, IV, V, VI, VII'''
            elif atom=='44' or atom.lower() == 'ruthenium':
                output='''
                Nomor atom= 44\n
                Golongan= VIII-B\n
                Nama atom : Ruthenium (Ru)\n
                Nama latin :  Ruthenium\n
                Nama Inggris : Ruthenium\n
                Penemu : Karl Ernst Claus\n
                Elektron : 44, Proton : 44, Neutron : 57\n
                Berat atom : 101.07 (g/mol)\n
                Fase : padat\n
                Perkiraan ion : Ru3+, Ru4+\n
                Valensi : II, III, IV, V, VI, VIII'''
            elif atom=='45' or atom.lower() == 'radium':
                output='''
                Nomor atom= 45\n
                Golongan= VIII-B\n
                Nama atom : Radium (Rh)\n
                Nama latin :  Rhodium\n
                Nama Inggris : Rhodium\n
                Penemu : William Hyde Wollaston\n
                Elektron : 45, Proton : 45, Neutron : 57\n
                Berat atom : 102.905 (g/mol)\n
                Fase : padat\n
                Perkiraan ion : Rh3+\n
                Valensi : III'''
            elif atom=='46' or atom.lower() == 'paladium':
                output='''
                Nomor atom= 46\n
                Golongan= VIII-B\n
                Nama atom : Paladium (Pd)\n
                Nama latin :  Palladium\n
                Nama Inggris : Palladium\n
                Penemu : William Hyde Wollaston\n
                Elektron : 46, Proton : 46, Neutron : 60\n
                Berat atom : 106.42 (g/mol)\n
                Fase : padat\n
                Perkiraan ion : Pd2+, Pd4+\n
                Valensi : 0, II, IV'''
            elif atom=='47' or atom.lower() == 'perak':
                output='''
                Nomor atom= 47\n
                Golongan= I-B\n
                Nama atom : Perak (Ag)\n
                Nama latin :  Argentum\n
                Nama Inggris : Silver\n
                Penemu : -\n
                Elektron : 47, Proton : 47, Neutron : 61\n
                Berat atom : 107.868 (g/mol)\n
                Fase : padat\n
                Perkiraan ion : Ag+\n
                Valensi : I, II, III'''
            elif atom=='48' or atom.lower() == 'kadmium':
                output='''
                Nomor atom= 48\n
                Golongan= II-B\n
                Nama atom : Kadmium (Cd)\n
                Nama latin :  Cadmium\n
                Nama Inggris : Cadmium\n
                Penemu : Friedrich Stromeyer\n
                Elektron : 48, Proton : 48, Neutron : 64\n
                Berat atom : 112.411 (g/mol)\n
                Fase : padat\n
                Perkiraan ion : Cd2+\n
                Valensi : II'''
            elif atom=='49' or atom.lower() == 'indium':
                output='''
                Nomor atom= 49\n
                Golongan= III-A\n
                Nama atom : Indium (In)\n
                Nama latin :  Indium\n
                Nama Inggris : Indium\n
                Penemu : Ferdinand Reich\n
                Elektron : 49, Proton : 49, Neutron : 66\n
                Berat atom : 114.818 (g/mol)\n
                Fase : padat\n
                Perkiraan ion : In3+\n
                Valensi : II, III'''
            elif atom=='50' or atom.lower() == 'timah':
                output='''
                Nomor atom= 50\n
                Golongan= IV-A\n
                Nama atom : Timah (Sn)\n
                Nama latin :  Stannum\n
                Nama Inggris : Tin\n
                Penemu : -\n
                Elektron : 50, Proton : 50, Neutron : 69\n
                Berat atom : 118.710 (g/mol)\n
                Fase : padat\n
                Perkiraan ion : Sn4+, Sn2+\n
                Valensi : II, IV'''
            elif atom=='51' or atom.lower() == 'antimon':
                output='''
                Nomor atom= 51\n
                Golongan= V-A\n
                Nama atom : Antimon (Sb)\n
                Nama latin :  Stibium\n
                Nama Inggris : Antimony\n
                Penemu : Basil Valentine\n
                Elektron : 51, Proton : 51, Neutron : 71\n
                Berat atom : 121.760 (g/mol)\n
                Fase : padat\n
                Perkiraan ion : Sb3+, Sb5+\n
                Valensi : III, V'''
            elif atom=='52' or atom.lower() == 'telurium':
                output='''
                Nomor atom= 52\n
                Golongan= VI-A\n
                Nama atom : Telurium (Te)\n
                Nama latin :  Tellurium\n
                Nama Inggris : Tellurium\n
                Penemu : -\n
                Elektron : 52, Proton : 52, Neutron : 75\n
                Berat atom : 127.60 (g/mol)\n
                Fase : padat\n
                Perkiraan ion : Te2-\n
                Valensi : II, IV, VI'''
            elif atom=='53' or atom.lower() == 'yodium':
                output='''
                Nomor atom= 53\n
                Golongan= VII-A\n
                Nama atom : Yodium (I)\n
                Nama latin :  Iodium\n
                Nama Inggris : Iodine\n
                Penemu : Bernard Courtois\n
                Elektron : 53, Proton : 53, Neutron : 74\n
                Berat atom : 126.904 (g/mol)\n
                Fase : padat\n
                Perkiraan ion : I-\n
                Valensi : I, III, V, VII'''
            elif atom=='54' or atom.lower() == 'xenon':
                output='''
                Nomor atom= 54\n
                Golongan= VIII-A\n
                Nama atom : Xenon (Xe)\n
                Nama latin :  Xenon \n
                Nama Inggris : Xenon\n
                Penemu : William Ramsey, Morris William Travers\n
                Elektron : 54, Proton : 54, Neutron : 77\n
                Berat atom : 131.293 (g/mol)\n
                Fase : Gas\n
                Perkiraan ion : -\n
                Valensi : 0'''
            else:
                st.error('nama dan nomor atom tidak terdapat di periode ini silahkan input yang lain!')
        st.write (output)

    if periode=='periode 6':
        atom= st.text_input ('masukkan nomor atom atau nama unsur')
        output=''
        if st.button('submit'):
            if atom=='55' or atom.lower() == 'sesium':
                output='''
                Nomor atom= 55\n
                Golongan= I-A\n
                Nama atom= Cs (Sesium)\n
                Nama latin= Caesium\n
                Nama inggris= Caesium\n
                Penemu= Robert Wilhelm Bunsen, Gustav Robert Kirchhoff\n
                Proton= 55, Elektron= 55, Neutron= 78\n
                Berat atom= 132.905 (g/mol)\n
                Fase= Solid\n
                Perkiraan ion= Cs+\n
                Valensi= I'''
            elif atom=='56' or atom.lower() == 'barium':
                output='''
                Nomor atom= 56\n
                Golongan= II=A\n
                Nama atom= Ba (Barium)\n
                Nama latin= Barium\n
                Nama inggris= Barium\n
                Penemu= Humphry Davy\n
                Proton= 56, Elektron= 56, Neutron= 81\n
                Berat atom= 137.327 (g/mol)\n
                Fase= Solid\n
                Perkiraan ion= Ba+\n
                Valensi= II'''
            elif atom=='72' or atom.lower() == 'hafnium':
                output='''
                Nomor atom= 72\n
                Golongan= IV-B\n
                Nama atom=Hf (Hafnium)\n
                Nama latin= Hafnium\n
                Nama inggris= Hafnium\n
                Penemu= Georg Karl von Hevesy, Dirk Coster\n
                Proton= 72\n
                Elektron= 72\n
                Neutron= 106\n
                Berat atom= 178.49 (g/mol)\n
                Fase= Solid\n
                Perkiraan ion= Hf4+\n
                Valensi= IV'''
            elif atom=='73' or atom.lower() == 'bariumum':
                output='''
                Nomor atom= 73\n
                Golongan= V-B\n
                Nama atom= Ta (Tantalum)\n
                Nama latin= Tantalum\n
                Nama inggris= Tantalum\n
                Penemu= First_opener81\n
                Proton= 73, Elektron= 73, Neutron= 108\n
                Berat atom= 180.947 (g/mol)\n
                Fase= Solid\n
                Perkiraan ion= Ta5+\n
                Valensi= II,III,IV,V'''
            elif atom=='74' or atom.lower() == 'tungsen':
                output='''
                Nomor atom= 74\n
                Golongan= VI-B\n
                Nama atom= W (Tungsten)\n
                Nama latin= Wolfranium\n
                Nama inggris= Tungsten\n
                Penemu= Carl Wilhelm Scheele\n
                Proton= 74, Elektron= 74, Neutron= 110\n
                Berat atom= 183.84 (g/mol)\n
                Fase= Solid\n
                Perkiraan ion= W6+\n
                Valensi= II,III,IV,V,VI'''
            elif atom=='75' or atom.lower() == 'renium':
                output='''
                Nomor atom= 75\n
                Golongan= VII-B\n
                Nama atom= Re (Renium)\n
                Nama latin= Rhenium\n
                Nama inggris= Rhenium\n
                Penemu= Ida Noddack, Walter Noddack, Otto Berg\n
                Proton= 75,Elektron= 75\n
                Neutron= 111\n
                Berat atom= 186.207 (g/mol)\n
                Fase= Solid\n
                Perkiraan ion= Re7+\n
                Valensi= I,II,III,IV,V,VI,VII'''
            elif atom=='76' or atom.lower() == 'osmium':
                output='''
                Nomor atom= 76\n
                Golongan= VIII-B\n
                Nama atom= Os (Osmium)\n
                Nama latin= Osmium\n
                Nama inggris= Osmium\n
                Penemu= Smithson Tennant\n
                Proton= 76, Elektron= 76, Neutron= 114\n
                Berat atom= 190.23 (g/mol)\n
                Fase= Solid\n
                Perkiraan ion= Os4+\n
                Valensi= III,IV,VIII'''
            elif atom=='77' or atom.lower() == 'iridium':
                output='''
                Nomor atom= 77\n
                Golongan= VIII-B\n
                Nama atom= Ir (Iridium)\n
                Nama latin= Iridium\n
                Nama inggris= Iridium\n
                Penemu= Smithson Tennant\n
                Proton= 77, Elektron= 77, Neutron= 115\n
                Berat atom= 192.217 (g/mol)\n
                Fase= Solid\n
                Perkiraan ion= Ir4+\n
                Valensi= I,II,III,IV,VI'''
            elif atom=='78' or atom.lower() == 'platina':
                output='''
                Nomor atom= 78\n
                Golongan= VIII-B\n
                Nama atom= Pt (Platina)\n
                Nama latin= Platinum\n
                Nama inggris= Platinum\n
                Penemu= Antonio de Ulloa\n
                Proton= 78, Elektron= 78, Neutron= 117\n
                Berat atom= 195.048 (g/mol)\n
                Fase= Solid\n
                Perkiraan ion= Pt4+, Pt2+\n
                Valensi= II,IV'''
            elif atom=='79' or atom.lower() == 'emas':
                output='''
                Nomor atom= 79\n
                Golongan= I-B\n
                Nama atom= Au (Emas)\n
                Nama latin= Aurum\n
                Nama inggris= Gold\n
                Penemu= -\n
                Proton= 79, Elektron= 79, Neutron= 118\n
                Berat atom= 196.966 (g/mol)\n
                Fase= Solid\n
                Perkiraan ion= Au3+, Au+\n
                Valensi= I,II,III'''
            elif atom=='80' or atom.lower() == 'raksa':
                output='''
                Nomor atom= 80\n
                Golongan= II-B\n
                Nama atom= Hg (Raksa)\n
                Nama latin= Hydrargyrum\n
                Nama inggris= Mercury\n
                Penemu= -\n
                Proton= 80, Elektron= 80, Neutron= 120\n
                Berat atom= 200.59 (g/mol)\n
                Fase= Liquid\n
                Perkiraan ion= Hg2+\n
                Valensi= I,II'''
            elif atom=='81' or atom.lower() == 'talium':
                output='''
                Nomor atom= 81\n
                Golongan= III-A\n
                Nama atom= Tl (Talium)\n
                Nama latin= Thallium\n
                Nama inggris= Thallium\n
                Penemu= William Crookes\n
                Proton= 81, Elektron= 81, Neutron= 123\n
                Berat atom= 204.383 (g/mol)\n
                Fase= Solid\n
                Perkiraan ion= Tl+, Tl3+\n
                Valensi= I,II,III'''
            elif atom=='82' or atom.lower() == 'timbal':
                output='''
                Nomor atom= 82\n
                Golongan= IV-A\n
                Nama atom= Pb (Timbal)\n
                Nama latin= Plumbum\n
                Nama inggris= Lead\n
                Penemu= -\n
                Proton= 82, Elektron= 82, Neutron= 125\n
                Berat atom= 207.2 (g/mol)\n
                Fase= Solid\n
                Perkiraan ion= Pb2+. Pb+\n
                Valensi= II,IV'''
            elif atom=='83' or atom.lower() == 'bismut':
                output='''
                Nomor atom= 83\n
                Golongan= V-A\n
                Nama atom= Bi (Bismut)\n
                Nama latin= Bisemutum (Bismuthum, Bismutum)\n
                Nama inggris= Bismuth\n
                Penemu= Claude Francois Geoffrey\n
                Proton= 83, Elektron= 83, Neutron= 126\n
                Berat atom= 208.9804 (g/mol)\n
                Fase= solid\n
                Perkiraan ion= Bi3+, Bi5+\n
                Valensi= III,V'''
            elif atom=='84' or atom.lower() == 'polonium':
                output='''
                Nomor atom= 84\n
                Golongan= VI-A\n
                Nama atom= Po (Polonium)\n
                Nama latin= Polonium\n
                Nama inggris= Polonium\n
                Penemu= Pierre Curie, Marie Skłodowska-Curie\n
                Proton= 84, Elektron= 84 , Neutron= 125\n
                Berat atom= 208.9824 (g/mol)\n
                Fase= Solid\n
                Perkiraan ion= Po2+, Po4+\n
                Valensi= II,IV,VI'''
            elif atom=='85' or atom.lower() == 'astatin':
                output='''
                Nomor atom= 85\n
                Golongan= VII-A\n
                Nama atom= At (Astatin)\n
                Nama latin= Astatum\n
                Nama inggris= Astatine\n
                Penemu= Paul Emile Lecod de Boisbaudran\n
                Proton= 85, Elektron= 85, Neutron= 125\n
                Berat atom= 209.9871 (g/mol)\n
                Fase= Solid\n
                Perkiraan ion= At-\n
                Valensi= -'''
            elif atom=='86' or atom.lower() == 'radon':
                output='''
                Nomor atom= 86\n
                Golongan= VIII-A\n
                Nama atom= Rn (Radon)\n
                Nama latin= Radon\n
                Nama inggris= Radon\n
                Penemu= Friedrich Ernst Dorn\n
                Proton= 86, Elektron= 86, Neutron= 136\n
                Berat atom= 222.0176 (g/mol)\n
                Fase= Gas\n
                Perkiraan ion= -\n
                Valensi=  0'''
            else:
                st.error('nama dan nomor atom tidak terdapat di periode ini silahkan input yang lain!')
        st.write (output)

    if periode=='periode 7':
        atom= st.text_input ('masukkan nomor atom atau nama unsur')
        output=''
        if st.button('submit'):
            if atom=='87' or atom.lower() == 'fransium':
                output='''
                Nomor atom= 87\n
                Golongan= I-A\n
                Nama atom=Fransium (fr)\n
                Nama latin=Francium\n
                Nama inggris=Francium\n
                Penemu=Marguerite perey\n
                Proton=87, Elektron=87, Neutron=136\n
                Berat atom=223.0197(g/mol)\n
                Fase=pada\n
                Perkiraan ion=Fe-\n
                Valensi=l'''
            elif atom=='88' or atom.lower() == 'radium':
                output='''
                Nomor atom= 88\n
                Golongan= II=A\n
                Nama atom=Radium (Ra)\n
                Nama latin=Radium\n
                Nama inggris=Radium\n
                Penemu: Pierre Curie, Marie Skłodowska Curie\n
                Proton=88, Elektron=88, Neutron=138\n
                Berat atom=226.0254(g/mol)\n
                Fase=padat\n
                Perkiraan ion=Ra²+\n
                Valensi=II'''
            elif atom=='104' or atom.lower() == 'rutherfordium':
                output='''
                Nomor atom= 104\n
                Golongan= IV-B\n
                Nama atom=Rutherfordium(Rf)\n
                Nama latin=Rutherfordium\n
                Nama inggris=Rutherfordium\n
                Penemu=Georgiy flerov\n
                Proton=104, Elektron=104, Neutron=157\n
                Berat atom=261.1087(g/mol)\n
                Fase=padat\n
                Perkiraan ion=-\n
                Valensi=-'''
            elif atom=='105' or atom.lower() == 'dubnium':
                output='''
                Nomor atom= 105\n
                Golongan= V-B\n
                Nama atom=Dubnium(Db)\n
                Nama latin=Dubnium\n
                Nama inggris=Dubnium\n
                Penemu=Georgiy Flerov\n
                Proton=105, Elektron=105, Neutron=157\n
                Berat atom=262.1138(g/mol)\n
                Fase=padat\n
                Perkiraan ion=-\n
                Valensi=-'''
            elif atom=='106' or atom.lower() == 'seaborgium':
                output='''
                Nomor atom= 106\n
                Golongan= VI-B\n
                Nama atom=seaborgium(sg)\n
                Nama latin=seaborgium\n
                Nama inggris=seaborgium\n
                Penemu=Georgiy Flerov\n
                Proton=106, Elektron=106, Neutron=163\n
                Berat atom=263.1182(g/mol)\n
                Fase=padat\n
                Perkiraan ion=-\n
                Valensi=-'''
            elif atom=='107' or atom.lower() == 'bohrium':
                output='''
                Nomor atom= 107\n
                Golongan= VII-B\n
                Nama atom=Bohrium (Bh)\n
                Nama latin=Bohrium\n
                Nama inggris=Bohrium\n
                Penemu: Peter Armbruster, Gottfried Munzenber\n
                Proton=107, Elektron=107, Neutron=160\n
                Berat atom=262.1269(g/mol)\n
                Fase=padat\n
                Perkiraan ion=-\n
                Valensi=-'''
            elif atom=='108' or atom.lower() == 'hassium':
                output='''
                Nomor atom= 108\n
                Golongan= VIII-B\n
                Nama atom=Hassium(Hs)\n
                Nama latin=Hassium\n
                Nama inggris=Hassium\n
                Penemu: GSI(Helmholtzzentrum für Schwerionenforschung)\n
                Proton=108, Elektron=108, Neutron=161\n
                Berat atom=269(g/mol)\n
                Fase=padat\n
                Perkiraan ion=-\n
                Valensi=-'''
            elif atom=='109' or atom.lower() == 'meitnerium':
                output='''
                Nomor atom= 109\n
                Golongan= VIII-B\n
                Nama atom=Meitnerium(Mt)\n
                Nama latin=Meitnerium\n
                Nama inggris=Meitnerium\n
                Penemu=GSI (Helmholtzzentrum für Schwerionenforschung)\n
                Proton=109, Elektron=109, Neutron=169\n
                Berat atom=278(g/mol)\n
                Fase=padat\n
                Perkiraan ion=-\n
                Valensi=-'''
            elif atom=='110' or atom.lower() == 'darmstadtium':
                output='''
                Nomor atom= 110\n
                Golongan= VIII-B\n
                Nama atom=Darmstadtium(Ds)\n
                Nama latin=Darmstadtium\n
                Nama inggris=Darmstadtium\n
                Penemu=GSI (Helmholtzzentrum für Schwerionenforschung)\n
                Proton=110, Elektron=110, Neutron=171\n
                Berat atom=281.1620(g/mol)\n
                Fase=padat\n
                Perkiraan ion=-\n
                Valensi=-'''
            elif atom=='111' or atom.lower() == 'roentgenium':
                output='''
                Nomor atom= 111\n
                Golongan= I-B\n
                Nama atom=Roentgenium(Rg)\n
                Nama latin=Roentgenium\n
                Nama inggris=Roentgenium\n
                Penemu=GSI (Helmholtzzentrum für Schwerionenforschung)\n
                Proton=111, Elektron=111, Neutron=171\n
                Berat atom=281.1684(g/mol)\n
                Fase=padat\n
                Perkiraan ion=-\n
                Valensi=-'''
            elif atom=='112' or atom.lower() == 'kopernesium':
                output='''
                Nomor atom= 112\n
                Golongan= II-B\n
                Nama atom=kopernesium(Cn)\n
                Nama latin=copernecium\n
                Nama inggris=copernecium\n
                Penemu=GSI (Helmholtzzentrum für Schwerionenforschung)\n
                Proton=112, Elektron=112, Neutron=173\n
                Berat atom=285.1744(g/mol)\n
                Fase=padat\n
                Perkiraan ion=-\n
                Valensi=-'''
            elif atom=='113' or atom.lower() == 'nihonium':
                output='''
                Nomor atom= 113\n
                Golongan= III-A\n
                Nama atom=Nihonium(Nh)\n
                Nama latin=Nihonium\n
                Nama inggris=Nihonium\n
                Penemu=RIKEN (理研)\n
                Proton=113, Elektron=113, Neutron=173\n
                Berat atom=286.1810(g/mol)\n
                Fase=padat\n
                Perkiraan ion=-\n
                Valensi=-'''
            elif atom=='114' or atom.lower() == 'flerovium':
                output='''
                Nomor atom= 114\n
                Golongan= IV-A\n
                Nama atom=Flerovium(Fi)\n
                Nama latin=Flerovium\n
                Nama inggris=Flerovium\n
                Penemu=Joint Institute for Nuclear Research (JINR)\n
                Proton=114, Elektron=114, Neutron=175\n
                Berat atom=287.1904(g/mol)\n
                Fase=padat\n
                Perkiraan ion=-\n
                Valensi=-'''
            elif atom=='115' or atom.lower() == 'moskovium':
                output='''
                Nomor atom= 115\n
                Golongan= V-A\n
                Nama atom=Moskovium(Mc)\n
                Nama latin=Moscovium\n
                Nama inggris=Moscovium\n
                Penemu= Joint Institute for Nuclear Research (JINR), Lawrence Livermore National Laboratory (LLNL)\n
                Proton=115, Elektron=115, Neutron=173\n
                Berat atom=288.1943(g/mol)\n
                Fase=padat\n
                Perkiraan ion=-\n
                Valensi=-'''
            elif atom=='116' or atom.lower() == 'livermorium':
                output='''
                Nomor atom= 116\n
                Golongan= VI-A\n
                Nama atom=Livermorium(Lv)\n
                Nama latin=Livermorium\n
                Nama inggris=Livermorium\n
                Penemu= Joint Institute for Nuclear Research (JINR), Lawrence Livermore National Laboratory (LLNL)\n
                Proton=116, Elektron=116, Neutron=177\n
                Berat atom=291.2045(g/mol)\n
                Fase=padat\n
                Perkiraan ion=-\n
                Valensi=-'''
            elif atom=='117' or atom.lower() == 'tenesin':
                output='''
                Nomor atom= 117\n
                Golongan= VII-A\n
                Nama atom=Tenesin(Ts)\n
                Nama latin=Tennessine\n
                Nama inggris=Tennessine\n
                Penemu= Joint Institute for Nuclear Research (JINR)\n
                Proton=117, Elektron=117, Neutron=177\n
                Berat atom=294.2104(g/mol)\n
                Fase=padat\n
                Perkiraan ion=-\n
                Valensi=-'''
            elif atom=='118' or atom.lower() == 'oganeson':
                output='''
                Nomor atom= 118\n
                Golongan= VIII-A\n
                Nama atom=Oganeson(Og)\n
                Nama latin=Oganneson\n
                Nama inggris=Oganneson\n
                Penemu= Joint Institute for Nuclear Research (JINR)\n
                Proton=118, Elektron=118, Neutron=176\n
                Berat atom=294.2139(g/mol)\n
                Fase=padat\n
                Perkiraan ion=-\n
                Valensi=-'''
        else:
                st.error('nama dan nomor atom tidak terdapat di periode ini silahkan input yang lain!')
        st.write (output)

if navbar == 'Simbol Bahaya dan Bahan Kimia':
    jenisbahan= st.selectbox('pilih simbol bahaya', options=['pilih simbol','Eksplosive','Oksidasi','Korosif','Berbahaya Bagi Lingkungan','Irritant','Toxic'])
    if jenisbahan=='Eksplosive':
        st.image('eksplosive.jpeg')
        st.write('''
        Pengertian: Eksplosive adalah Bahan kimia yang mudah meledak apabila terkena benturan, gesekan, pemanasan, sumber api maupun sumber nyala lainnya. Bahkan tanpa oksigen pun, bahan ini mudah meledak.\n
        Pencegahan: Hindari penempatan dengan bahan lain yang mudah bereaksi dan simpan ditempat yang aman''')
        contohbahan= st.selectbox('pilih contoh bahan', options=['pilih bahan','Amonium nitrat (NH4NO3)','Nitro selulosa [C6H7O2(ONO2)3]','TNT (C7H5N3O6)','Nitrogliserin (C3H5N3O9)'])
        if contohbahan== 'Amonium nitrat (NH4NO3)' :
            st.write('''
            Nama bahan : Amonium nitrat (NH4NO3)\n
            Sifat : mudah meledak\n
            Bereaksi dengan : logam hidroksida\n
            Wujud\n
            - warna : putih
            - bau : tidak berbau
            - wujud fisik : padatan kristal''')
        elif contohbahan== 'Nitro selulosa [C6H7O2(ONO2)3]':
            st.write('''
            Nama bahan : nitro selulosa [C6H7O2(ONO2)3]\n
            Sifat : mudah meledak\n
            Bereaksi dengan : reaksi selulosa dengan cara sibsitusi gugus -OH dengan gugus -ONO2\n
            Wujud \n
            - warna : putih kekuningan
            - bau : bau khas nitro selulosa
            - wujud fisik : serbuk (hablur)''')
        elif contohbahan== 'TNT (C7H5N3O6)':
            st.write('''
            Nama bahan : TNT (C7H5N3O6)\n
            Sifat : mudah meledak\n
            Bereaksi dengan :  toluena bereaksi dengan HNO3 menggunakan katalis H2SO4\n
            Wujud \n
            - warna : kuning pucat
            - bau : beraroma menyengat
            - wujud fisik : padatan''')
        elif contohbahan== 'Nitrogliserin (C3H5N3O9)':
            st.write('''
            Nama bahan : nitrogliserin (C3H5N3O9)\n
            Sifat : mudah meledak\n
            Bereaksi dengan : gliserin bereaksi dengan HNO3 menggunakan katalis H2SO4\n
            Wujud \n
            - warna : tidak berwarna
            - bau : bau khas nitrogliserin
            - wujud fisik : cairan''')

    elif jenisbahan=='Oksidasi':
        st.image('oksidasi.jpeg')
        st.write('''
        Pengertian: Oksidasi memiliki sifat yang mudah terbakar jika terjadi kontak langsung dengan bahan organik atau bahan pereduksi yang mampu menghasilkan panas.\n
        Pencegahan: Hindari kontak langsung dengan bahan yang bereaksi dan mengatur penyimpanan sebaik mungkin''')
        contohbahan= st.selectbox('pilih contoh bahan', options=['pilih bahan','Kalium klorat (KCLO3)','Kalium permanganat (KMNO4)','Kalium dikromat (K2Cr2O7)','Peroksida (H2O2)'])
        if contohbahan== 'Kalium klorat (KCLO3)':
            st.write('''  
            Nama bahan : kalium klorat (KCLO3)\n
            Sifat : pengoksidasi\n
            Bereaksi dengan : asam sulfat\n
            Wujud \n
            - warna : putih
            - bau : bau khas kalium klorat
            - wujud fisik : padatan kristal
            ''')
        elif contohbahan== 'Kalium permanganat (KMNO4)':
            st.write('''
            Nama bahan : kalium permanganat (KMNO4)\n
            Sifat : pengoksidasi\n
            Bereaksi dengan : senyawa yang mudah menyala\n
            Wujud \n
            - warna : ungu
            - bau : bau khas kalium permanganat
            - wujud fisik : cairan''')
        elif contohbahan== 'Kalium dikromat (K2Cr2O7)':
            st.write('''
            Nama bahan : kalium dikromat (K2Cr2O7)\n
            Sifat : pengoksidasi\n
            Bereaksi dengan : larutan asam klorida (HCl)
            Wujud 
            - warna : merah keorange
            - bau : bau khas kalium dikromat
            - wujud fisik : padatan kristal''')
        elif contohbahan== 'Peroksida (H2O2)':
            st.write('''
            Nama bahan : peroksida (H2O2)
            Sifat : pengoksidasi
            Bereaksi dengan : perak oksida
            Wujud 
            - warna : tidak berwarna 
            - bau : bau khas peroksida
            - wujud fisik : cairan''')

    elif jenisbahan=='Korosif':
        st.image('korosif.jpeg')
        st.write('''
        Pengertian: Korosif adalah bahan kimia ini memiliki sifat korosif dengan nilai pH sebesar < 2 atau > 12.5. Bahan kimia korosif dapat mengiritasi kulit hingga merusak jaringan hidup.\n
        Pencegahan: Hindari bahan dari kontak langsung dengan kulit.''')
        contohbahan= st.selectbox('pilih contoh bahan', options=['pilih bahan','Asam klorida (HCl)','Asam sulfat (H2SO4)','Natrium Hidroksida (NaOH)'])
        if contohbahan== 'Asam klorida (HCl)':
            st.write(''' 
            Nama bahan : asam klorida (HCl)\n
            Sifat : korosif\n
            wujud\n
            - Wujud fisik : cair
            - Bau : khas asam klorida
            - Warna : keruh''')
        elif contohbahan== 'Asam sulfat (H2SO4)':
            st.write('''
            Nama bahan=asam sulfat(H2SO4)\n
            Sifat = korosif\n
            Wujud \n
            - Wujud fisik= cair
            - Warna= bening
            - Bau=khas asam sulfat''')
        elif contohbahan== 'Natrium Hidroksida (NaOH)':
            st.write('''
            Nama bahan=Natrium Hidroksida (NaOH)\n
            Sifat= korosif\n
            wujud\n
            - Wujud fisik = kristal padatan
            - Warna = putih
            - Bau = khas Naoh''')
    elif jenisbahan=='Berbahaya Bagi Lingkungan':
        st.image('berbahaya bagi lingkungan.jpeg')
        st.write('''
        Pengertian: Berbahaya Bagi Lingkungan Bahan kimia ini mampu menyebabkan penurunan kualitas lingkungan dan mengganggu keseimbangan ekologi akibat kandungannya yang berbahaya.\n
        Pencegahan: Dapat dilakukan dengan membuang bahan tersebut pada tempat khusus dan tidak lupa untuk memisahkannya''')
        contohbahan= st.selectbox('pilih contoh bahan', options=['pilih bahan','Karbon monoksida (CO)','Amonia (NH3)','Asam sulfat (H2SO4)','Asam klorida (HCl)'])
        if contohbahan== 'Karbon monoksida (CO)':
            st.write('''
            Nama bahan=karbon monoksida(CO)\n
            Sifat = berbahaya bagi lingkungan\n
            wujud\n
            - Wujud fisik =gas
            - Bau = tidak berbau
            - Warna = tidak bewarna''')
        elif contohbahan== 'Amonia (NH3)':
            st.write('''   
            Nama bahan=Amonia\n
            Sifat = berbahaya bagi lingkungan\n
            wujud\n
            - Wujud fisik = gas
            - Warna = tidak bewarna
            - Bau = sangat menyengat''')
        elif contohbahan== 'Asam sulfat (H2SO4)':
            st.write(''' 
            Nama bahan= asam sulfat\n
            Sifat= berbahaya bagi lingkungan\n
            wujud\n
            - Warna=bening
            - Wujud fisik = cair
            - Bau= khas asam sulfat''')
        elif contohbahan== 'Asam klorida (HCl)':
            st.write('''
            Nama bahan=asam klorida\n
            Sifat=berhahaya bagi lingkungan\n
            wujud\n
            - Wujud fisik = cair
            - Warna= keruh
            - Bau= khas asam klorida''')
    elif jenisbahan=='Irritant':
        st.image('irritant.jpeg')
        st.write('''
        Pengertian: Irritant adalah bahan yang dapat menyebabkan inflamasi jika kontak langsung dengan selaput lendir atau kulit tetapi, bahan kimia ini tidak bersifat korosif. Efek yang ditimbulkan seperti gatal-gatal hingga luka bakar kecil pada kulit.\n
        Pencegahan: Menggunakan masker dan sarung tangan.''')
        contohbahan= st.selectbox('pilih contoh bahan', options=['pilih bahan','Kalsium klorida (CaCl2)','Natrium hidroksida (NaOH)','Diklorometana (CH2Cl2)','Etilen glikol (C2H6O2)','Toluena (C6H5CH3)'])
        if contohbahan== 'Kalsium klorida (CaCl2)':
            st.write('''
            Nama bahan: Kalsium klorida (CaCl2)\n
            Sifat: irritant\n
            wujud\n
            - Wujud fisik: padatan
            - Warna: putih 
            - Bau: tidak berbau''')
        elif contohbahan== 'Natrium hidroksida (NaOH)':
            st.write('''
            Nama bahan: Natrium hidroksida\n
            Sifat: irritant\n
            wujud
            - Wujud fisik: padatan
            - Warna: putih
            - Bau: tidak berbau''')
        elif contohbahan== 'Diklorometana (CH2Cl2)':
            st.write('''
            Nama bahan: diklorometana (CH2Cl2)\n
            Sifat: irritant\n
            wujud\n
            Wujud fisik: cairan
            Warna: tak bewarna
            Bau: manis''')
        elif contohbahan== 'Etilen glikol (C2H6O2)':
            st.write('''
            Nama bahan: Etilen glikol\n
            Sifat: irritant\n
            wujud\n
            Wujud fisik: cairan
            Warna: tidak bewarna
            Bau: tidak berbau''')
        elif contohbahan== 'Toluena (C6H5CH3)':
            st.write('''
            Nama bahan: toluena\n
            Sifat: irritant\n
            wujud\n
            Wujud fisik: Cairan
            Warna: tidak bewarna
            Bau: seperti pengencer cat''')
    elif jenisbahan=='Toxic':
        st.image('toxic.jpeg')
        st.write('''
        Pengertian: Bahan toxic apat menyebabkan efek kerusakan kesehatan yang akut bahkan kematian meskipun terjadi kontak (melalui hidung, kulit, dan mulut) dalam konsentrasi yang rendah.\n
        Pencegahan: Hindari kontak terlalu sering dan menggunakan APD lengkap ''')
        contohbahan= st.selectbox('pilih contoh bahan', options=['pilih bahan','Karbon Tetraklorida (CCl4)','Benzena (C6H6)','Nitro Benzena (C6H5NO2)','Kalium Sianida (KCN)','Mercury (Hg)'])
        if contohbahan== 'Karbon Tetraklorida (CCl4)':
            st.write('''
            Nama bahan: Karbon Tetraklorida\n
            Sifat: Toxic\n
            wujud\n
            Wujud fisik: cairan
            Warna: tidak bewarna
            Bau: Manis''')
        elif contohbahan== 'Benzena (C6H6)':
            st.write('''
            Nama bahan: Benzena\n
            Sifat: Toxic\n
            wujud\n
            Wujud fisik: Cairan
            Warna: tidak bewarna
            Bau: manis''')
        elif contohbahan== 'Nitro Benzena (C6H5NO2)':
            st.write('''
            Nama bahan: Nitro Benzena\n
            Sifat: Toxic\n
            wujud\n
            Wujud fisik: cairan
            Warna: Kuning pucat 
            Bau: seperti buah almond''')
        elif contohbahan== 'Kalium Sianida (KCN)':
            st.write('''
            Nama bahan: Kalium Sianida\n
            Sifat: Toxic\n
            wujud\n
            Wujud fisik: Padatan Krital 
            Warna: putih
            Bau: bau khas almond pahit''')
        elif contohbahan== 'Mercury (Hg)':
            st.write('''
            Nama bahan: Mercury\n
            Sifat: Toxic\n
            wujud\n
            Wujud fisik: Cairan
            Warna: putih perak
            Bau: tak berbau''')