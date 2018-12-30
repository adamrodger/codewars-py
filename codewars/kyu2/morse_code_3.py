# https://www.codewars.com/kata/decode-the-morse-code-for-real/train/python
# https://en.wikipedia.org/wiki/K-means_clustering

import re

def calculateClusters(samples):
    """
    Group the samples into up to 3 clusters and return a dict of cluster
    mean to samples in the cluster
    """
    # assign the samples to a cluster then move the cluster towards the mean of the samples
    converged = False

    # randomly seed the appropriate number of clusters
    unique_lengths = set([len(x) for x in samples])
    cluster_count = min(3, len(unique_lengths))

    if cluster_count == 1:
        # everything is the same length
        return { len(samples[0]): samples }
    elif cluster_count == 2:
        # just start at the extremes and work inwards
        clusters = { min(unique_lengths): [], max(unique_lengths): []}
    else:
        # start clusters at min, average and max lengths
        clusters = { min(unique_lengths): [], sum(unique_lengths) / len(unique_lengths): [], max(unique_lengths): []}
    
    while not converged:
        converged = True

        # assign
        for sample in samples:
            closest_distance = 999999.0
            closest_centroid = 999999.0

            for centroid in clusters.keys():
                distance = abs(len(sample) - centroid)

                if distance < closest_distance:
                    closest_distance = distance
                    closest_centroid = centroid

            clusters[closest_centroid].append(sample)

        # move centroids
        moved_clusters = {}

        for centroid, members in clusters.items():
            if not members:
                continue # drop this cluster

            mean = float(sum([len(x) for x in members])) / float(len(members)) # python 2.x support
            moved_clusters[mean] = []
            if mean != centroid:
                converged = False

        if not converged:    
            clusters = moved_clusters

    return clusters

def decodeBitsAdvanced(bits):
    """
    Decodes a string of 0s and 1s of irregular lengths to equivalent Morse Code
    in dots and dashes
    """

    bits = bits.strip("0")

    if not bits:
        return ""
    
    samples = re.findall("1+|0+", bits)
    clusters = calculateClusters(samples)

    # clusters now contains the converged means of the 3 clusters and the samples assigned
    thresholds = sorted(clusters.keys())
    result = ""

    # find which cluster the sample belongs to and translate to dot/dash/char separator/word separator
    for sample in samples:
        if sample in clusters[thresholds[0]]:
            result += "." if sample[0] == "1" else ""
        elif sample in clusters[thresholds[1]]:
            result += "-" if sample[0] == "1" else " "
        elif sample in clusters[thresholds[2]]:
            result += "-" if sample[0] == "1" else "   "
        else:
            raise ValueError("Unknown cluster for sample {}".format(sample))

    return result

def decodeMorse(morseCode):
    """
    Decodes a message encoded in dots and dashes with character and word separators
    """
    words = morseCode.strip().split('   ')
    return " ".join(["".join([MORSE_CODE[letter] for letter in word.split()]) for word in words])

MORSE_CODE={'.-...': '&',
            '--..--': ',',
            '....-': '4',
            '.....': '5',
            '...---...': 'SOS',
            '-...': 'B',
            '-..-': 'X',
            '.-.': 'R',
            '.--': 'W',
            '..---': '2',
            '.-': 'A',
            '..': 'I',
            '..-.': 'F',
            '.': 'E',
            '.-..': 'L',
            '...': 'S',
            '..-': 'U',
            '..--..': '?',
            '.----': '1',
            '-.-': 'K',
            '-..': 'D',
            '-....': '6',
            '-...-': '=',
            '---': 'O',
            '.--.': 'P',
            '.-.-.-': '.',
            '--': 'M',
            '-.': 'N',
            '....': 'H',
            '.----.': "'",
            '...-': 'V',
            '--...': '7',
            '-.-.-.': ';',
            '-....-': '-',
            '..--.-': '_',
            '-.--.-': ')',
            '-.-.--': '!',
            '--.': 'G',
            '--.-': 'Q',
            '--..': 'Z',
            '-..-.': '/',
            '.-.-.': '+',
            '-.-.': 'C',
            '---...': ':',
            '-.--': 'Y',
            '-': 'T',
            '.--.-.': '@',
            '...-..-': '$',
            '.---': 'J',
            '-----': '0',
            '----.': '9',
            '.-..-.': '"',
            '-.--.': '(',
            '---..': '8',
            '...--': '3'}
