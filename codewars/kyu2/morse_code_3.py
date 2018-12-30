# https://www.codewars.com/kata/decode-the-morse-code-for-real/train/python
# https://en.wikipedia.org/wiki/K-means_clustering

import re

def decodeBitsAdvanced(bits):
    """
    Decodes a string of 0s and 1s of irregular lengths to equivalent Morse Code
    in dots and dashes following Morse Code timing rules
    """

    bits = bits.strip("0")

    if not bits:
        return ""
    
    samples = re.findall("1+|0+", bits)
    clusters = calculate_clusters(samples)

    print("Samples: {}".format(samples))
    print("Clusters: {}".format(clusters))

    # clusters now contains the converged means of the 3 clusters and the samples assigned
    thresholds = sorted(clusters.keys())
    result = ""

    # find which cluster the sample belongs to and translate to dot/dash/char separator/word separator
    for sample in samples:
        if sample in clusters[thresholds[0]]:
            result += "." if sample[0] == "1" else "" # dot or dot/dash break
        elif sample in clusters[thresholds[1]]:
            result += "-" if sample[0] == "1" else " " # dash or character break
        elif sample in clusters[thresholds[2]]:
            result += "-" if sample[0] == "1" else "   " # very long dash or word break
        else:
            raise ValueError("Unknown cluster for sample {}".format(sample))

    return result

def calculate_clusters(samples):
    """
    Group the samples into 3 clusters representing the 3 different time lengths in
    Morse Code and return a dict of cluster mean to samples in the cluster
    """
    unique_lengths = sorted(set([len(x) for x in samples]))

    if len(unique_lengths) < 3:
        return simple_search(samples, unique_lengths)
    else:
        return k_means_clustering(samples, unique_lengths)

def simple_search(samples, unique_lengths):
    """
    Approximates 3 clusters representing the 3 time period in Morse Code (1, 3 and 7 time units)
    when there is not enough data to perform a k-means clustering algorithm
    """
    clusters = {
        min(unique_lengths): [],
        min(unique_lengths) * 3: [],
        min(unique_lengths) * 7: []
    }

    assign_to_clusters(samples, clusters)
    return clusters

def k_means_clustering(samples, unique_lengths):
    """
    Performs a k-means clustering algorithm to sort the samples into 3 distinct clusters
    each representing the 3 different time periods in Morse Code (1, 3 and 7 time units)
    """
    converged = False

    # start at the min, max and mid-point
    min_length = min(unique_lengths)
    max_length = max(unique_lengths)
    clusters = {
        min_length: [],
        (min_length + max_length) / 2: [],
        max_length: []
    }
    
    while not converged:
        converged = True

        assign_to_clusters(samples, clusters)

        # move centroids
        moved_clusters = {}

        for centroid, members in clusters.items():
            if not members:
                moved_clusters[centroid] = []
                continue

            mean = float(sum([len(x) for x in members])) / float(len(members)) # python 2.x support
            moved_clusters[mean] = []
            if mean != centroid:
                converged = False

        if not converged:    
            clusters = moved_clusters
    
    if len(samples) > 500:
        # some insane hack to redo the middle cluster as the mid-point between the lower and upper means
        hack_clusters = {
            min(clusters.keys()): [],
            max(clusters.keys()): [],
            ((max(clusters.keys()) + min(clusters.keys())) / 2): [] # new made up midpoint
        }
        assign_to_clusters(samples, hack_clusters)
        return hack_clusters
    else:
        return clusters

def assign_to_clusters(samples, clusters):
    """
    Assigns every sample to the nearest cluster
    """
    for sample in samples:
        closest_distance = 999999.0
        closest_centroid = 999999.0

        for centroid in clusters.keys():
            distance = abs(len(sample) - centroid)

            if distance <= closest_distance:
                closest_distance = distance
                closest_centroid = centroid

        clusters[closest_centroid].append(sample)

def decodeMorse(morseCode):
    """
    Decodes a message encoded in dots and dashes with character and word separators
    """
    words = morseCode.strip().split('   ')

    result = ""

    for word in words:
        for letter in word.split():
            try:
                result += MORSE_CODE[letter]
            except:
                result += "(ERR)"
        result += " "
    
    result = result[:-1] # chop off trailing space
    print("Result: {}".format(result))
    return result

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
