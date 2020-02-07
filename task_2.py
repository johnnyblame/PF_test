import json
import fire


class Json_Reader:
    try:
        with open('schema.json', 'r') as file:
            data = json.load(file)
    except FileNotFoundError:
        JSON_TEMPLATE = { "connections": {}, "access": []}
        with open('schema.json', 'w') as file:
            json.dump(JSON_TEMPLATE, file)
            file.close()
        with open('schema.json', 'r') as outfile:
            data = json.load(outfile)

    @staticmethod
    def path_rebuilder(path):
        true_path = path.split('/')
        return true_path

    def get(self, path):
        '''
        :param path: looks like 'path/to/key/'
        :return:
        '''
        curr_path = self.path_rebuilder(path)
        if len(curr_path) == 3:
            needed = self.data[curr_path[0]][curr_path[1]][curr_path[2]]
        elif len(curr_path) == 2:
            needed = self.data[curr_path[0]][curr_path[1]]
        else:
            needed = self.data[curr_path[0]]
        return needed

    def set(self, path, val):
        curr_path = self.path_rebuilder(path)
        if len(curr_path) == 3:
            self.data[curr_path[0]][curr_path[1]][curr_path[2]] = val
        elif len(curr_path) == 2:
            self.data[curr_path[0]][curr_path[1]] = val
        else:
            self.data[curr_path[0]] = val

        with open('schema.json', 'w') as file:
            json.dump(self.data, file, indent=4)
        return ''


if __name__ == '__main__':
    fire.Fire(Json_Reader)
