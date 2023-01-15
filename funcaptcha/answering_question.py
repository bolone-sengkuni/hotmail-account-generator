import matplotlib.pyplot as plt
import numpy as np
import librosa
import librosa.display

# loads the audio and turns it into a list of numbers


# # TODO: qual das opcções altera a voz.
def question_1():
    for i in range(3):
        answer_number = 0
        answer_number += 1

        data, fs = librosa.load(f'sounds/{i}.wav')
        D = librosa.amplitude_to_db(np.abs(librosa.stft(data)))

        x = 0
        for i in range(2):
            v = len(D[1])

            for ii in range(v):
                if ii + 1 == v:
                    break
                
                if (D[i][ii] - D[i][ii + 1]) <= D[i][ii] - 10 or (D[i][ii] - D[i][ii + 1]) >= D[i][ii] + 10:
                    x += 1
            
            if x > 120:
                return answer_number
            return False