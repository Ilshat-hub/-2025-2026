"""Задание 3: Функция для перевода градусов Цельсия в Фаренгейт. Напишите
функцию celsius_to_fahrenheit(celsius), которая принимает температуру в
градусах Цельсия и возвращает её эквивалент в градусах Фаренгейта. (Формула: F
= C * 9/5 + 32)"""
def celsius_to_fahrenheit(celsius):
    return celsius * 9/5 + 32

print(celsius_to_fahrenheit(1))