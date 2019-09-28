def createConfig():
    config = {}
    config["x0"] = .1
    config["y0"] = .1
    config["z0"] = .1
    config["evaluateNum"] = 100000
    config["leftBound"] = config["evaluateNum"] // 4
    config["rightBound"] = config["evaluateNum"]

    return config