from helpers.problemrunner import run_problem
from enum import Enum

@run_problem
def run():
    with open("Problem0031.txt") as f:
        hex_transmission = f.readlines()[0]
    parser = TransmissionParser()
    parser.parse(hex_transmission)

    return sum(parser.versions)


class TransmissionParser():

    def parse(self, hexCode):
        self.binary_data = bin(int(hexCode, 16))[2:] # remove '0b'
        zero_fill = len(self.binary_data) + 4 - len(bin(int(hexCode[0], 16))[2:])
        self.binary_data = self.binary_data.zfill(zero_fill) # add missing leading zeros
        self.position = 0
        self.versions = []
        self.packet()


    def packet(self):
        if self.header() == PacketType.LITERAL:
            self.literal_value()
        else:
            self.operator_packet()
        # Ignore trailing 0s


    def header(self):
        self.versions.append(self.version())
        return self.type_id()


    def version(self):
        return self.to_int(self.read_and_proceed(3))


    def type_id(self):
        return PacketType.LITERAL if self.to_int(self.read_and_proceed(3)) == 4 else PacketType.OPERATOR


    def literal_value(self):
        last = False
        value = ''
        while not last:
            last = self.to_int(self.read_and_proceed(1)) == 0
            value += self.read_group()


    def read_group(self):
        return self.read_and_proceed(4)


    def operator_packet(self):
        if self.length_type_id() == LengthTypeId.TOTALLENGTH:
            length = self.to_int(self.read_and_proceed(15))
            self.read_total_length_packets(length)
        else:
            count = self.to_int(self.read_and_proceed(11))
            self.read_number_of_packets(count)


    def length_type_id(self):
        return LengthTypeId.TOTALLENGTH if self.to_int(self.read_and_proceed(1)) == 0 else LengthTypeId.SUBPACKAGES


    def read_total_length_packets(self, length):
        current_position = self.position
        while self.position - current_position < length:
            self.packet()


    def read_number_of_packets(self, count):
        for _ in range(count):
            self.packet()


    def read_and_proceed(self, count):
        ret = self.binary_data[self.position:self.position + count]
        self.position += count
        return ret


    def to_int(self, binary):
        return int(binary, 2)


class PacketType(Enum):
    LITERAL = 1,
    OPERATOR = 2


class LengthTypeId(Enum):
    TOTALLENGTH = 1,
    SUBPACKAGES = 2

run()
