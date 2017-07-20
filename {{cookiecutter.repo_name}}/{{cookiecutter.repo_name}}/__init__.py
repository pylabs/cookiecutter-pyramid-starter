from pyramid.config import Configurator


def main(global_config, **settings):
    """ This function returns a Pyramid WSGI application.
    """
    config = Configurator(settings=settings)
    config.include('pyramid_jinja2')

    # session settings
    #
    # using builtin session mechanism
    #from pyramid.session import SignedCookieSessionFactory
    #config.set_session_factory(SignedCookieSessionFactory(settings['secret_key']))

    config.add_static_view('static', 'static', cache_max_age=3600)
    config.add_route('home', '/')
    config.scan()
    return config.make_wsgi_app()
