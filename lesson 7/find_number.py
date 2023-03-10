
def find_numd(num):
    count = num - 1
    avgfloors = 5
    numb_flats = 4

    H_search = count // (numb_flats * avgfloors)
    F_search = (count - (numb_flats*avgfloors)*(H_search)) // numb_flats

    return f"під'їзд: {H_search + 1}, поверх: {F_search + 1}, квартира: {num}"

search = 61

print(find_numd(search))
