import numpy as np
from tqdm import tqdm
import forecast_generator as fg
import weather_data_extractor as we
import weather_xml_generator as mx

FILE_NAME = "weather.xml"


def main():

    print("Script downloads current weather files and creates xml for the servers")

    files = we.download_files()
    raw = [we.convert_weather_file(f) for f in files]
    weather = []
    for r in raw:
        weather.extend(r)

    print("Processing {} weather reports".format(len(weather)))

    print("Generating forecasts")
    # batching so we can have a progress bar
    batchsize = 100
    batches = []
    for i in tqdm(range(0, len(weather), batchsize)):
        fc_batch = fg.make_forecasts(np.array(weather[i:i+batchsize]))
        #  get list of packs (24x forecasts per origin)
        batches.append([fc for sublist in fc_batch for fc in sublist])

    forecasts = [fc for batch in batches for fc in batch]

    print("Generating forecasts complete. Creating XML")
    document = mx.make_data_document(forecasts, weather)

    xml_file = open(FILE_NAME, 'w')
    xml_file.write(document.toxml())
    xml_file.close()
    print("File {} created. Goodbye".format(FILE_NAME))



if __name__ == '__main__':
    main()