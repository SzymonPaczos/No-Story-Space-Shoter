#ifndef ASSETSMANAGER_H
#define ASSETSMANAGER_H


class AssetsManager
{
    private:
        AssetsManager();
        AssetsManager( const App & _app) = delete;




    public:
        void operator=(const App &) = delete;
        static App & getInstance()
        {
            static AssetsManager _am;
            return _am;
        }

};

#endif // ASSETSMANAGER_H
