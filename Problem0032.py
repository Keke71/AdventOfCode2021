from helpers.problemrunner import run_problem
from enum import IntEnum
from functools import reduce


@run_problem
def run():
    with open("Problem0032.txt") as f:
        hex_transmission = list(line.rstrip() for line in f)[0]
    parser = TransmissionParser()
    
    return parser.parse(hex_transmission)


class Operator():

    def sum(values):
        return sum(values)

    def product(values):
        return reduce(lambda a, b: a * b, values)

    def minimum(values):
        return min(values)

    def maximum(values):
        return max(values)

    def greater_than(values):
        return 1 if values[0] > values[1] else 0

    def less_than(values):
        return 1 if values[0] < values[1] else 0

    def equal_to(values):
        return 1 if values[0] == values[1] else 0

# Start: Packet
#
#                   / Literal Value
# Packet: Header ->
#                   \ Operator Packet
#
# Header: Version (3 bits) - PacketType (3 bits)
#
# Literal Value: {[0|1] Group} +
#
# Group: 4 bits
#
#                                        / TotalLength (15 bits)       \
# Operator Packet: LengthType (1 bit) ->                                 ->  {Packet} +
#                                        \ Number of packets (11 bits) /
class TransmissionParser():
    operators = [
        Operator.sum,
        Operator.product,
        Operator.minimum,
        Operator.maximum,
        None,
        Operator.greater_than,
        Operator.less_than,
        Operator.equal_to
    ]

    def parse(self, hexCode):
        # Leading zeros are completely ignored
        length = len(hexCode)
        expected_length = length * 4
        self.binary_data = bin(int(hexCode, 16))[2:] # remove '0b'
        self.binary_data = self.binary_data.zfill(expected_length) # add missing leading zeros
        self.position = 0

        return self.packet()


    def packet(self):
        _, packet_type = self.header()
        if packet_type == PacketType.LITERAL:
            return self.literal_value()
        else:
            return self.operator_packet(packet_type)


    def header(self):
        # version + type id
        return (self.version(), self.type_id())


    def version(self):
        # 3 bits version
        return self.to_int(self.read_bits(3))


    def type_id(self):
        # 3 bits type id
        return PacketType(self.to_int(self.read_bits(3)))


    def literal_value(self):
        last = False
        value = ''
        while not last:
            # First bit 0: last group; otherwise more groups will follow
            last = self.to_int(self.read_bits(1)) == 0
            value += self.group()

        return self.to_int(value)


    def group(self):
        # 4-bit integer value
        return self.read_bits(4)


    def operator_packet(self, packet_type):
        operator = TransmissionParser.operators[packet_type]
        if self.length_type_id() == LengthType.TOTALLENGTH:
            # length is stored in a 15-bit value
            length = self.to_int(self.read_bits(15))
            return self.read_total_length_packets(length, operator)
        else:
            # number of packets is stored in an 11-bit value
            count = self.to_int(self.read_bits(11))
            return self.read_number_of_packets(count, operator)


    def length_type_id(self):
        # 1 bit length type id
        return LengthType(self.to_int(self.read_bits(1)))


    def read_total_length_packets(self, length, operator):
        current_position = self.position
        values = []
        while self.position - current_position < length:
            # read subpackages and collect their results
            values.append(self.packet())

        # calculate result of values
        return operator(values)


    def read_number_of_packets(self, count, operator):
        values = []
        for _ in range(count):
            # read subpackages and collect their results
            values.append(self.packet())

        # calculate result of values
        return operator(values)


    def read_bits(self, count):
        ret = self.binary_data[self.position : self.position + count]
        self.position += count
        return ret


    def to_int(self, binary):
        return int(binary, 2)


class PacketType(IntEnum):
    SUM = 0,
    PRODUCT = 1,
    MINIMUM = 2,
    MAXIMUM = 3,
    LITERAL = 4,
    GREATERTHAN = 5,
    LESSTHAN = 6,
    EQUALTO = 7


class LengthType(IntEnum):
    TOTALLENGTH = 0,
    SUBPACKAGES = 1


run()
