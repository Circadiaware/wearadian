# Wearadian
Non-invasive wearable circadian rhythm telemonitoring sensors.

# Description
This project aims to provide a complete set of clinical-grade devices to monitor over the long-term (1 week to a year) various factors that are well-established in influencing or reflecting the circadian rhythm. In clinical jargon, the aim is to devise wearables for the non-invasive ambulatory supervised monitoring and self-monitoring of human circadian rhythm.

Indeed, there is a lack of both accurate and non-invasive and durable devices to monitor the human circadian rhythm: often, the devices are invasive (such as for core body temperature sensing), or are inaccurate (wrist PPG instead of ECG, low sampling rate), and even when these two criteria are met, most devices cannot last at least 24h, which makes them unusable to monitor a full circadian cycle, especially for circadian rhythm disorders such as non-24 where one cycle can be much longer than 24h. However, to allow for self-monitoring of the circadian rhythm, a device needs to fulfill at least these 3 criteria (and more). This project aims to provide a set of devices to capture most of the biological signals that can objectively reflect or affect the human circadian rhythm.

To achieve that, we repurpose off-the-shelf components and devices where possible, or create new ones with DIY Arduino boards where necessary. This repository will contain all the instructions to detail what components and devices are necessary, how to use them, and for the custom devices the hardware and software source codes are provided. Softwares to visualize and (rudimentarily) analyze the generated data is also provided.

The whole documentation is in the `docs` folder licensed under CC-BY-SA 4.0 and can be read here:
https://circadiaware.github.io/wearadian/docs/Wearadian.html

The Wearadian version 1 design was ued to acquire the data of the longest running continuously biomarkers-monitored circadian rhythm sleep-wake experiment yet as of March 2024, with the full database of the completed first and a half year of data collection (with some biomarkers covering a much longer timespan) published on FigShare under the [MyNon24Sleep project](https://figshare.com/projects/MyNon24Sleep_-_A_self-study_of_the_circadian_rhythm_and_its_altering_factors/101804), licensed under Creative Commons BY 4.0 (CC BY 4.0).

A new version 2 of the Wearadian design, which better accommodates a natural, out of lab setting, is also described in the Wearadian technical documentation (this repository), and was partially collected and published on FigShare under the [MyNon24Sleep v2 project](https://figshare.com/projects/MyNon24Sleep_v2/142817), but was halted midway due to sensors malfunctions due to time wear anda lack of fundings (if you are interested in funding this research, please contact me on my [ResearchGate profile](https://www.researchgate.net/profile/Stephen-Larroque) or on [Reddit private messages](https://www.reddit.com/message/compose/?to=lrq3000)).

Alpha scripts to visualize and process the dataset can be found in the `Circalizer` project:
https://github.com/Circadiaware/circalizer

## Current state

All wearables except the light color sensor are implemented, and are being actively used to collect data.

There is one light sensor already in the actigraphic device, but it only measures light intensity and is placed on the wrist, which is suboptimal to reflect the exposure of the eyes to bright light.

## Future improvements

* Finish making the light intensity and color sensor using a custom program on an Adalogger/Arduino board (help is welcome!).
* Implementing a 9-axis actigraph, ie with absolute orientation in the space, would allow for a more precise characterization of positions (ie, did the subject stayed laid down during a time period? Does this correlate with body temperature changes?).

## Author

This project was started by Stephen Karl Larroque.

## License
All the documentation of this project (except for 3rd party's documentation such as the devices' providers') is under Creative Commons v4.0 with attribution and share-alike (CC-BY-SA 4.0). The source codes of custom devices and analysis softwares are under General Public License v3.0 (GPLv3).
