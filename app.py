import sys

from social.facebook import Facebook
from social.twitter import Twitter
from social.gmail import Gmail


def run():
        
    if len(sys.argv) != 2:
        sys.exit('Syntax: %s COMMAND' % sys.argv[0])
     
    cmd = sys.argv[1].lower()
    
    # initialize services
    facebook = Facebook('facebook', pid_dir='/tmp')
    twitter = Twitter('twitter', pid_dir='/tmp')
    gmail = Gmail('gmail', pid_dir='/tmp')
    
    if cmd == 'start':
        # start services
        facebook.start()
        twitter.start()
        gmail.start()
        print("Started all services")
    elif cmd == 'stop':
        # stop services
        facebook.stop()
        twitter.stop()
        gmail.stop()
        print("Stopped all services")
    elif cmd == 'status':
        print("Facebook service running: %s" % facebook.is_running())
        print("Twitter service running: %s" % twitter.is_running())
        print("Gmail service running: %s" % gmail.is_running())
    else:
        print('Unknown command "%s"' % cmd)

if __name__ == '__main__':
    run()

