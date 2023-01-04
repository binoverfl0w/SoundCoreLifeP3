import socket
from enum import Enum

class LifeP3Client:
    
    def __init__(self, address, port = 5):
        self.address = address
        self.port = port
        self.loadCommands()

    def loadCommands(self):
        self.commandlist = (
            # Noise canncellation modes
            Command(CommandType.NOISE, "08ee00000006810e00000001008c", "Noise Cancellation - Transport"),
            Command(CommandType.NOISE, "08ee00000006810e00000101008d", "Noise Cancellation - Outdoor"),
            Command(CommandType.NOISE,"08ee00000006810e00000201008e", "Noise Cancellation - Indoor"),
            Command(CommandType.NOISE,"08ee00000006810e00010100008d", "Transparency Mode - Fully Transparent"),
            Command(CommandType.NOISE,"08ee00000006810e00010101008e", "Transparency Mode - Vocal Mode"),
            Command(CommandType.NOISE,"08ee00000006810e00020101008f", "Normal"),
        
            # Equalizer modes
            Command(CommandType.EQUALIZER,"08ee000000028334000000787878787878787878007878787878787878780078787878787878787800787878787878787878008f", \
                            "Soundcore's signature - Bass Up OFF"),
            Command(CommandType.EQUALIZER,"08ee000000028334000200a0968278787878787800a09682787878787878007b7a78787878787878007b7a78787878787878003b", \
                            "Soundcore's signature - Bass Up ON"), 
            Command(CommandType.EQUALIZER,"08ee000000028334000100a0828c8ca0a0a08c7800a0828c8ca0a0a08c78007d767b787c7a7c7978007d767b787c7a7c7978007e", \
                        "Acoustic"),
            Command(CommandType.EQUALIZER,"08ee000000028334000300505a6e78787878787800505a6e787878787878007576787878787878780075767878787878787800e8", \
                            "Bass Reducer"),
            Command(CommandType.EQUALIZER,"08ee00000002833400040096966464788c96a0780096966464788c96a078007a7c7477787a797d78007a7c7477787a797d780081", \
                            "Classical"),
            Command(CommandType.EQUALIZER,"08ee0000000283340005005a8ca0a0968c786478005a8ca0a0968c78647800747b7a7b797a78757800747b7a7b797a7875780064", \
                        "Podcast"),
            Command(CommandType.EQUALIZER,"08ee0000000283340006008c5a6e828c8c825a78008c5a6e828c8c825a78007c7378787a797b7378007c7378787a797b737800a9", \
                    "Dance"),
            Command(CommandType.EQUALIZER,"08ee0000000283340007008c8296968c64504678008c8296968c64504678007a777b797b76767378007a777b797b767673780094",
                    "Deep"),
            Command(CommandType.EQUALIZER,"08ee000000028334000800968c648c828c96967800968c648c828c969678007a7b737d777a7a7b78007a7b737d777a7a7b7800c5", \
                            "Electronic"),
            Command(CommandType.EQUALIZER,"08ee00000002833400090064646e7878786464780064646e787878646478007677777878797676780076777778787976767800d6", \
                    "Flat"),
            Command(CommandType.EQUALIZER,"08ee000000028334000a008c966e6e8c6e8c9678008c966e6e8c6e8c967800797c76767d747b7b7800797c76767d747b7b78005d", \
                        "Hip-Hop"),
            Command(CommandType.EQUALIZER,"08ee000000028334000b008c8c6464788c96a078008c8c6464788c96a07800797b7577787a797d7800797b7577787a797d78005e", \
                    "Jazz"),
            Command(CommandType.EQUALIZER,"08ee000000028334000c0078786464647896aa780078786464647896aa78007879767776787a7e78007879767776787a7e7800cb", \
                    "Latin"),
            Command(CommandType.EQUALIZER,"08ee000000028334000d006e8ca09678648c8278006e8ca09678648c827800767a7b7a78747c787800767a7b7a78747c7878005a", \
                        "Longue"),
            Command(CommandType.EQUALIZER,"08ee000000028334000e007896968ca0aa96a078007896968ca0aa96a07800777b7a787b7c787d7800777b7a787b7c787d78009d", \
                        "Piano"),
            Command(CommandType.EQUALIZER,"08ee000000028334000f006e829696826e645a78006e829696826e645a780077797a7a79777775780077797a7a797777757800b2", \
                    "Pop"),
            Command(CommandType.EQUALIZER,"08ee000000028334001000b48c64648c9696a07800b48c64648c9696a078007e7976757b7a797d78007e7976757b7a797d7800f9", \
                    "R&B"),
            Command(CommandType.EQUALIZER,"08ee000000028334001100968c6e6e829696967800968c6e6e8296969678007a7a7677787b7a7b78007a7a7677787b7a7b7800b6", \
                    "Rock"),
            Command(CommandType.EQUALIZER,"08ee000000028334001200a0968278645a50507800a0968278645a505078007b7a78797676757478007b7a787976767574780033", \
                            "Small Speakers"),
            Command(CommandType.EQUALIZER,"08ee0000000283340013005a64828c8c82785a78005a64828c8c82785a780076767a797a787974780076767a797a787974780076", \
                            "Spoken Word"),
            Command(CommandType.EQUALIZER,"08ee0000000283340014006464646e828c8ca078006464646e828c8ca0780076777777797a787d780076777777797a787d7800d1", \
                                "Treble Booster"),
            Command(CommandType.EQUALIZER,"08ee000000028334001500787878645a50503c7800787878645a50503c780078787976777577717800787879767775777178000e", \
                                "Treble Reducer")
        )

    def send(self, command):
        self.socket.send(command.payload)

    def open(self):
        self.socket = socket.socket(socket.AF_BLUETOOTH, socket.SOCK_STREAM, socket.BTPROTO_RFCOMM)
        self.socket.connect((self.address, self.port))

    def close(self):
        self.socket.close()

    def getCommandList(self):
        return self.commandlist


class Command:
        def __init__(self, type, payloadstr, desc):
            self.type = type
            self.payload = bytes.fromhex(payloadstr)
            self.desc = desc

class CommandType(Enum):
    NOISE = 1
    EQUALIZER = 2