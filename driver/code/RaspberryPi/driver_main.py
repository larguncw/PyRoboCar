from py_robo_car import PyRoboCar
import logging
import sys

def main():
    # print system info
    logging.info('Starting DeepPiCar, system info: ' + sys.version)
    
    with PyRoboCar() as car:
        car.drive(40)
    
if __name__ == '__main__':
    logging.basicConfig(level=logging.DEBUG)
    main()
