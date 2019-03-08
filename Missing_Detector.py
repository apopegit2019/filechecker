import getopt
import os
import time
import sys

arglst = sys.argv[1:]


def opt_parse(arglst):
    try:
        opts, args = getopt.getopt(arglst, 'hf:t:o:', ['--help', '--feed', '--target', '--output'])
    except getopt.GetoptError:
        print('-f for feed file location \n -t for target folder \n -o for output location \n --help \n --feed \n '
              '--target \n --output \n \n')
    if opts == '-h':
        print('-f for feed file location \n -t for target folder \n -o for output location \n --help \n --feed \n '
              '--target \n --output \n \n')
    if opts in ('-f', '--feed'):
        feedloc = args
    if opts in ('-o', '--output'):
        outloc = args
    if opts in ('-t', '--target'):
        targloc = args
    if os.path.isdir(targloc):
        print('The target folder to be searched: %s \n' % targloc)
    else:
        print('Target Directory Does Not Exist.')
        exit()
    if os.path.isdir(outloc):
        print('Output will be saved to %s \n' % outloc)
    else:
        print('Target Directory Does Not Exist.')
        exit()
    if os.path.isfile(feedloc):
        print('Feed file location is: %s \n' % feedloc)
    else:
        print('Target Directory Does Not Exist.')
        exit()
    uanswer = input('Are these correct and are you ready to proceed? (Y/N) \n')
    if uanswer in ('y', 'Y', 'Yes', 'YES'):
        filecheck(feedloc, outloc, targloc)
    else:
        print('Try again')
        exit()


def flength(feedloc):
    with open(feedloc, 'r') as feed:
        length = feed.readlines()
    return length


def mklog(outloc):
    logname = 'outlog' + time.strftime('%Y%m%d%H%M') + '.log'
    logpath = os.path.join(outloc, logname)
    if os.path.isfile(logpath):
        logname = 'outlog' + time.strftime('%Y%m%d%H%M%S') + '.log'
        logpath = os.path.join(outloc, logname)
        return
    else:
        return logpath


def logging(logfile, lmsg):
    msg = time.ctime() + ' :  %s \n' % lmsg
    with open(logfile, 'a+') as log:
        log.write(msg)


def target(feedloc, targloc, feedlen, lpath):
    current = 0
    found = 0
    ntfound = 0
    with open(feedloc, 'r') as feed:
        for line in feed:
            current += 1
            line = line.rstrip('\n')
            logging(lpath, 'Checking %d/%d: %s' % (feedlen, current, line))
            file = os.path.join(targloc, line)
            if os.path.isfile(file):
                logging(lpath, '%s exists')
                found += 1
            else:
                logging(lpath, '%s NOT FOUND' % line)
                ntfound += 1
    return found, ntfound


def filecheck(feedloc, outloc, targloc):
    lpath = mklog(outloc)
    feedlen = flength(feedloc)
    logging(lpath, 'Feed has %d entries. \n' % feedlen)
    fnd, nfnd = target(feedloc, targloc, feedlen, lpath)
    logging(lpath, 'Feed Complete')
    logging(lpath, 'Found %d Files' % fnd)
    logging(lpath, '%d Files Missing' % nfnd)
    print('Check Complete \n')
    exit()


opt_parse(arglst)
