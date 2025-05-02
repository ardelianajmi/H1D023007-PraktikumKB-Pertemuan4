% File: pakar_jerawat.pl

:- dynamic gejala_pos/1.
:- dynamic gejala_neg/1.

penyakit("Jerawat Meradang").
penyakit("Jerawat Pasir").
penyakit("Jerawat Batu").
penyakit("Jerawat Komedo").

% Gejala
gejala(kemerahan, "Jerawat Meradang").
gejala(bengkak, "Jerawat Meradang").
gejala(perih, "Jerawat Meradang").

gejala(bintik_kecil, "Jerawat Pasir").
gejala(kulit_kasar, "Jerawat Pasir").
gejala(gatal, "Jerawat Pasir").

gejala(benjolan_besar, "Jerawat Batu").
gejala(nyeri_saat_disentuh, "Jerawat Batu").
gejala(susah_hilang, "Jerawat Batu").

gejala(komedo_putih, "Jerawat Komedo").
gejala(komedo_hitam, "Jerawat Komedo").
gejala(kulit_berminyak, "Jerawat Komedo").

% Pertanyaan
pertanyaan(kemerahan, "Apakah kulit tampak merah dan meradang?").
pertanyaan(bengkak, "Apakah terdapat pembengkakan pada jerawat?").
pertanyaan(perih, "Apakah terasa perih di area jerawat?").

pertanyaan(bintik_kecil, "Apakah terdapat bintik-bintik kecil di wajah?").
pertanyaan(kulit_kasar, "Apakah kulit terasa kasar saat diraba?").
pertanyaan(gatal, "Apakah jerawat terasa gatal?").

pertanyaan(benjolan_besar, "Apakah terdapat benjolan besar di wajah?").
pertanyaan(nyeri_saat_disentuh, "Apakah terasa nyeri saat disentuh?").
pertanyaan(susah_hilang, "Apakah jerawat susah hilang dalam waktu lama?").

pertanyaan(komedo_putih, "Apakah Anda memiliki komedo putih?").
pertanyaan(komedo_hitam, "Apakah Anda memiliki komedo hitam?").
pertanyaan(kulit_berminyak, "Apakah kulit Anda sangat berminyak?").
