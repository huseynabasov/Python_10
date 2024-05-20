# #Part 1
# import os
# import shutil

# # 1. "Example" adinda bir directory yaratmaq
# example_dir = "Example"
# os.makedirs(example_dir, exist_ok=True)

# # 2. Bu directory-nin içerisinde bir "subdirect" adinda alt directory yaratmaq
# subdirect_dir = os.path.join(example_dir, "subdirect")
# os.makedirs(subdirect_dir, exist_ok=True)

# # 3. sekil ve text faylini "subdirect" qovluğuna elave etmek
# # sekli ilk önce manual olaraq hazirda olduğunuz qovluğa sürüsdürmüsünüz, meselen "image.jpg"
# # Text faylini yaratmaq ve subdirect qovluğuna köçürmek
# image_file = "image.jpg"
# if os.path.exists(image_file):
#     shutil.move(image_file, os.path.join(subdirect_dir, image_file))
# else:
#     print(f"sekil fayli '{image_file}' tapilmadi. Lütfen, sekli manual olaraq cari qovluğa elave edin.")

# text_file = "example.txt"
# with open("example.txt", mode="w", encoding="utf-8") as test:
#     test.write("salam")
# shutil.move(text_file, os.path.join(subdirect_dir, text_file))

# # 4. subdirect içerisinde olan ve sonu .txt ile biten fayllari Example directory-sine köçürmek
# for file_name in os.listdir(subdirect_dir):
#     if file_name.endswith(".txt"):
#         shutil.move(os.path.join(subdirect_dir, file_name), os.path.join(example_dir, file_name))

# print("emeliyyat uğurla tamamlandi.")


# =======================================================================================================================================

# Part 2

# def yerleri_tap(xallar):
#     xal_indeks = list(enumerate(xallar))
#     siralanmis_xal_indeks = sorted(xal_indeks, key=lambda x: x[1], reverse=True)
#     yerler = [0] * len(xallar)
#     for sira, (index, xal) in enumerate(siralanmis_xal_indeks):
#         yerler[index] = f"{sira + 1}-ci"

#     return yerler


# xallar = [1, 3, 4, 2, 5]
# print(yerleri_tap(xallar))
