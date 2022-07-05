# Noisy Neighbour

Noise levels in flat 1/1 measured with a zoom H4 ambient sound
recorder. Sensitivity set to "high" (=night time).

Every peak represents an exercise weight hitting the floor in flat 0/1 below.

## Sound levels from 2:27am *before* the police visited him

![alt tag](Loudness_5_July_from_2_27.png)

Six "thuds" can be heard at:
```
Thud #1 at 2022-07-05 03:29:17.704000
Thud #2 at 2022-07-05 03:35:41.230000
Thud #3 at 2022-07-05 03:36:09.062000
Thud #4 at 2022-07-05 03:42:26.758000
Thud #5 at 2022-07-05 03:47:19.490000
Thud #6 at 2022-07-05 03:50:59.026000
```

## Sound levels from 4:38am *after* the police visited him

*Constantly* throwing exercise weights on the floor with
much higher intensity so that the recorder went *off scale* (=1).

![alt tag](Loudness_5_July_from_4_38.png)

15 "thuds" can be heard at:
```
Thud #1 at 2022-07-05 04:39:03.480000
Thud #2 at 2022-07-05 04:40:39.554000
Thud #3 at 2022-07-05 04:45:26.616000
Thud #4 at 2022-07-05 04:46:34.620000
Thud #5 at 2022-07-05 04:47:41.088000
Thud #6 at 2022-07-05 04:48:52.190000
Thud #7 at 2022-07-05 04:55:00.964000
Thud #8 at 2022-07-05 04:56:31.194000
Thud #9 at 2022-07-05 04:59:08.744000
Thud #10 at 2022-07-05 05:01:20.080000
Thud #11 at 2022-07-05 05:02:22.460000
Thud #12 at 2022-07-05 05:04:31.166000
Thud #13 at 2022-07-05 05:06:58.936000
Thud #14 at 2022-07-05 05:08:57.520000
Thud #15 at 2022-07-05 05:11:19.898000
```

## Sound files

Original recordings were at 44kHz sampling rate.

To be able to load the ~1hr WAV into python it was downsampled to
500Hz sampling rate to focus on the low base frequencies or "thuds":

```
sox STE-038_2_27_5jul.wav -c 1 -r 500 STE-038_2_27_5jul_500Hz.wav
sox STE-039_4_38_5jul.wav -c 1 -r 500 STE-039_4_38_5jul_500Hz.wav
```
