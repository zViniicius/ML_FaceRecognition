from pathlib import Path

import cv2
import face_recognition
import numpy as np


def load_known_faces(images_dir, character_images):
    """
    Carrega as imagens dos personagens e gera as codificações dos rostos.

    :param images_dir: Diretório contendo as imagens dos personagens.
    :param character_images: Dicionário com os nomes e os arquivos das imagens.

    :return: Listas de codificações e nomes dos rostos conhecidos.
    """
    known_face_encodings = []
    known_face_names = []

    for name, filename in character_images.items():
        image_path = images_dir / filename
        try:
            image = face_recognition.load_image_file(image_path)
            encodings = face_recognition.face_encodings(image)

            if encodings:
                known_face_encodings.append(encodings[0])
                known_face_names.append(name)
            else:
                print(f"Aviso: Nenhum rosto detectado em {filename}.")
        except Exception as e:
            print(f"Erro ao carregar a imagem {filename}: {e}")

    return known_face_encodings, known_face_names


def recognize_faces_in_image(input_image, known_face_encodings, known_face_names):
    """
    Reconhece rostos em uma imagem e retorna os nomes dos rostos detectados.

    :param input_image: Imagem de entrada no formato BGR (como lida pelo OpenCV).
    :param known_face_encodings: Codificações dos rostos conhecidos.
    :param known_face_names: Nomes dos rostos conhecidos.

    :return: Lista de nomes dos rostos detectados.
    """
    rgb_image = cv2.cvtColor(input_image, cv2.COLOR_BGR2RGB)

    face_locations = face_recognition.face_locations(rgb_image)
    face_encodings = face_recognition.face_encodings(rgb_image, face_locations)

    face_names = []

    for face_encoding in face_encodings:
        matches = face_recognition.compare_faces(known_face_encodings, face_encoding)
        name = "Desconhecido"

        face_distances = face_recognition.face_distance(known_face_encodings, face_encoding)
        best_match_index = np.argmin(face_distances)

        if matches[best_match_index]:
            name = known_face_names[best_match_index]

        face_names.append(name)

    return face_locations, face_names


def annotate_image(image, face_locations, face_names):
    """
    Adiciona caixas delimitadoras e nomes aos rostos detectados na imagem.

    :param image: Imagem a ser anotada.
    :param face_locations: Localizações dos rostos detectados.
    :param face_names: Nomes dos rostos detectados.

    :return: Imagem anotada.
    """
    for (top, right, bottom, left), name in zip(face_locations, face_names):
        cv2.rectangle(image, (left, top), (right, bottom), (0, 0, 255), 2)

        cv2.rectangle(image, (left, bottom - 20), (right, bottom), (0, 0, 255), cv2.FILLED)

        font = cv2.FONT_HERSHEY_DUPLEX
        cv2.putText(image, name, (left + 6, bottom - 6), font, 0.5, (255, 255, 255), 1)

    return image


def main():
    input_dir = Path('input')
    output_dir = Path('output')
    images_dir = Path('assets/images')
    output_dir.mkdir(parents=True, exist_ok=True)

    character_images = {}

    for image_path in images_dir.glob('*.jpg'):
        character_name = image_path.stem
        character_images[character_name] = image_path.name

    known_face_encodings, known_face_names = load_known_faces(images_dir, character_images)

    input_image_path = input_dir / 'image.jpg'  # Imagem de entrada
    image = cv2.imread(str(input_image_path))

    if image is None:
        print(f"Erro: Não foi possível carregar a imagem {input_image_path}")
        return

    face_locations, face_names = recognize_faces_in_image(image, known_face_encodings, known_face_names)

    annotated_image = annotate_image(image, face_locations, face_names)

    output_image_path = output_dir / f'recognized_faces_out.jpg'
    cv2.imwrite(str(output_image_path), annotated_image)

    recognized_count = sum(1 for name in face_names if name != "Desconhecido")
    unknown_count = len(face_names) - recognized_count

    print(f"Rostos reconhecidos: {recognized_count}")
    print(f"Rostos desconhecidos: {unknown_count}")
    print(f"Imagem anotada salva em: {output_image_path}")


if __name__ == "__main__":
    main()
