#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2017 Adrián López Tejedor <adrianlzt@gmail.com>
#                  Óscar García Amor <ogarcia@connectical.com>
#
# Distributed under terms of the GNU GPLv3 license.

from colorama import init, Fore
from tabulate import tabulate

import sys

# Initialize colorama
init(strip=not sys.stdout.isatty())

def print_workspaces(workspaces):
    ws_table = []
    for workspace in workspaces:
         ws_table.append([workspace.id, workspace.name, workspace.description])
    print (tabulate(ws_table, headers=['ID', 'Name', 'Description'], tablefmt="rst"))

def print_vaults(vaults):
    v_table = []
    colors = {
            'blue': Fore.BLUE,
            'orange': Fore.YELLOW,
            'purple': Fore.MAGENTA,
            'green': Fore.GREEN,
            'red': Fore.RED
            }
    for vault in vaults:
        id = colors[vault.color] + str(vault.id) + Fore.RESET
        v_table.append([id, vault.name, vault.description])
    print (tabulate(v_table, headers=['ID', 'Name', 'Description'], tablefmt="rst"))

def print_cards(cards):
    c_table = []
    for card in cards:
        c_table.append([card.id, card.name, card.description])
    print (tabulate(c_table, headers=['ID', 'Name', 'Description'], tablefmt="rst"))

def print_secrets(secrets):
    s_table = []
    types = {
            100: 'Note',
            200: 'Password',
            300: 'File'
            }
    for secret in secrets:
        s_table.append([secret.id, secret.name, types[secret.type]])
    print (tabulate(s_table, headers=['ID', 'Name', 'Secret type'], tablefmt="rst"))

def print_secret(secret):
    s_table =[['Name', secret.name]]
    if secret.data:
        if 'url' in secret.data: s_table.append(['URL', secret.data['url']])
        if 'username' in secret.data: s_table.append(['Username', secret.data['username']])
        if 'password' in secret.data: s_table.append(['Password', secret.data['password']])
    if secret.blobMeta:
        s_table.append(['File Name', secret.blobMeta['filename']])
        s_table.append(['File Size', '{} B'.format(secret.blobMeta['filesize'])])
    if secret.data and 'note' in secret.data: s_table.append(['Note', secret.data['note']])
    print (tabulate(s_table, headers="firstrow", tablefmt="rst"))
