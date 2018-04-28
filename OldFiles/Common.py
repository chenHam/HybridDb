from OldFiles import powerSetFinder as psf


def getColumnsPowerSet(columns):
    return psf.listToPowerset(columns)

def getFromConfiguration(config, name, var):
    try:
        return config.get(name)[var]
    except Exception as e:
        e1 = str(e)
        print("Exception: " + e1)
        return ""