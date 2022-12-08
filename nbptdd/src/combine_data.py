from dataclasses import dataclass


@dataclass
class CombineData():
    

    def get_list_of_dicts(self, data: dict) -> list[dict]:
        if isinstance(data, dict):
            one_layer_data = {key:data[key] for key in data if not isinstance(data[key], list)}
            list_of_dicts = []
            for k, v in data.items():
                if isinstance(v, list):
                    for sub_dict in v:
                        product = one_layer_data | sub_dict
                        list_of_dicts.append(product)
            return list_of_dicts
        else:
            return None


    def union_dicts(self, list_a: list[dict], list_b: list[dict]) -> list[dict]:
        if isinstance(list_a, list) and isinstance(list_b, list):
            product = list_a + list_b
            final_product = []
            for item in product:
                if isinstance(item, dict):
                    final_product.append(item)
            return final_product
        else:
            return None
