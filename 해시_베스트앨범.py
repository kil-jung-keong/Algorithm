from collections import defaultdict
genres = ["classic", "pop", "classic", "classic", "pop"]
plays = [500, 600, 150, 800, 2500]
music_dict = defaultdict(list)
music = []
for i in range(len(genres)):
    music.append([i,genres[i],plays[i]])
for i,k,v in music:
    music_dict[k].append([v,i])
for key in music_dict.keys():
    music_dict[key].sort(reverse=True)
print(music_dict)
for key in music_dict.keys():
    print(music_dict[key][:2][-1])