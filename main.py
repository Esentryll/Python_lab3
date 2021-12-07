from read_file import read_file
from write_file import write_file
from sort import insertion_sort
from serialaizer import SerialaizeWriter
from serialaizer import SerialaizeReader
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('--input', type=str, default="D:\\valid.txt", help='Input path')
parser.add_argument('--output', type=str, default="deserialized.txt", help='Output path')
args = parser.parse_args()

ser_arr = insertion_sort(read_file(args.input).read_file())
writer = SerialaizeWriter('data.json')
writer.write_file(ser_arr)
print("Serialized data is written")

read_ser = SerialaizeReader('data.json')
arr_ser = read_ser.read_file()
print("Serialized data is read")
writer = write_file(args.output)
writer.write_file(arr_ser)
print("Deserialized data is written")











