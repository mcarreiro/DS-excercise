import csv


class CSVFileSaver:

    def save(self, file_name, object_list):
        with open(file_name, 'w+') as csv_file:
            wr = csv.writer(csv_file, delimiter=",")

            keys = self.keys(object_list[0])

            # Write title
            wr.writerow(keys)

            for cd in object_list:
                wr.writerow(self.values(cd,keys))


    def keys(self, cd):
        return vars(cd).keys()

    def values(self, cd, keys):
        values = []
        for key in keys:
            values.append(getattr(cd, key))
        return values

