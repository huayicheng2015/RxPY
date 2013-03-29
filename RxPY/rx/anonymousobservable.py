from .autodetachobserver import AutoDetachObserver
from .observable import Observable

class AnonymousObservable(Observable):
    def __init__(self, subscribe):
        def s(observer):
            auto_detach_observer = AutoDetachObserver(observer)
            if False: #current_thread_scheduler.schedule_tequired()):
                def action():
                    try:
                        auto_detach_observer.disposable(subscribe(auto_detach_observer))
                    except Exception as ex:
                        if not auto_detach_observer.fail(e):
                            raise e
                current_thread_scheduler.schedule(action)
            else:
                try:
                    auto_detach_observer.disposable(subscribe(auto_detach_observer))
                except Exception as ex:
                    if not auto_detach_observer.fail(e):
                        raise e

            return auto_detach_observer
        
        super(AnonymousObservable, self).__init__(s)
    