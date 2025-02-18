import cv2
import mediapipe as mp
import yaml


class HandFaceMeshApp:
    def __init__(self, config_path):

        with open(config_path, 'r') as file:
            self.config = yaml.safe_load(file)

        self.cap = cv2.VideoCapture(self.config['video_source'])

        # Hand tracking setup
        self.mp_hands = mp.solutions.hands
        self.hands = self.mp_hands.Hands(
            min_detection_confidence=self.config['min_detection_confidence'],
            min_tracking_confidence=self.config['min_tracking_confidence'])
        self.mp_drawing = mp.solutions.drawing_utils

        # Face Mesh setup
        self.mp_face_mesh = mp.solutions.face_mesh
        self.face_mesh = self.mp_face_mesh.FaceMesh(
            min_detection_confidence=self.config['face_min_detection_confidence'],
            min_tracking_confidence=self.config['face_min_tracking_confidence'])


        self.hand_drawing_spec = self.mp_drawing.DrawingSpec(color=(0, 255, 0), thickness=2, circle_radius=3)
        self.face_drawing_spec = self.mp_drawing.DrawingSpec(color=(255, 0, 0), thickness=2, circle_radius=5)

    def process_frame(self, image):
        image = cv2.flip(image, 1)
        rgb_image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)


        hand_results = self.hands.process(rgb_image)
        if hand_results.multi_hand_landmarks:
            self.draw_hand_landmarks(image, hand_results)


        face_results = self.face_mesh.process(rgb_image)
        if face_results.multi_face_landmarks:
            self.draw_face_landmarks(image, face_results)

        return image

    def draw_hand_landmarks(self, image, hand_results):
        """Draws hand landmarks separately from face mesh."""
        for hand_landmarks in hand_results.multi_hand_landmarks:
            for id, lm in enumerate(hand_landmarks.landmark):
                h, w, _ = image.shape
                cx, cy = int(lm.x * w), int(lm.y * h)


                if id in [4, 8, 12, 16, 20]:
                    cv2.circle(image, (cx, cy), 10, (255, 255, 255), cv2.FILLED)


            self.mp_drawing.draw_landmarks(
                image, hand_landmarks, self.mp_hands.HAND_CONNECTIONS,
                self.hand_drawing_spec, self.hand_drawing_spec)

    def draw_face_landmarks(self, image, face_results):

        h, w, _ = image.shape

        offset_x = 500

        for face_landmarks in face_results.multi_face_landmarks:
            for landmark in face_landmarks.landmark:
                cx, cy = int(landmark.x * w), int(landmark.y * h)


                cx_offset = min(cx + offset_x, w - 1)
                cv2.circle(image, (cx_offset, cy), 5, (255, 255, 0),
                           -1)

            for connection in self.mp_face_mesh.FACEMESH_CONTOURS:
                start_idx, end_idx = connection
                start = face_landmarks.landmark[start_idx]
                end = face_landmarks.landmark[end_idx]

                start_x, start_y = int(start.x * w) + offset_x, int(start.y * h)
                end_x, end_y = int(end.x * w) + offset_x, int(end.y * h)


                start_x, end_x = min(start_x, w - 1), min(end_x, w - 1)


                cv2.line(image, (start_x, start_y), (end_x, end_y), (0, 255, 255), 2)

    def run(self):
        while self.cap.isOpened():
            success, image = self.cap.read()
            if not success:
                print("Ignoring empty camera frame.")
                continue

            image = self.process_frame(image)
            cv2.imshow('Hand and Face Mesh', image)

            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

        self.cap.release()
        cv2.destroyAllWindows()


if __name__ == "__main__":
    app = HandFaceMeshApp('config.yaml')
    app.run()



