#ifndef ASSETSMANAGER_H
#define ASSETSMANAGER_H
#include <SFML/Graphics.hpp>
#include <SFML/System.hpp>
#include <memory>
#include <string>
class AssetsManager
{
    private:
        AssetsManager();
<<<<<<< HEAD
        AssetsManager( const AssetsManager & _am) = delete;
    public:
        static AssetsManager & getInstance();
        void operator=(const AssetsManager &) = delete;
        std::shared_ptr<sf::Texture> getTexture(std::string _path);
=======
        AssetsManager( const App & _app) = delete;




    public:
        void operator=(const App &) = delete;
        static App & getInstance()
        {
            static AssetsManager _am;
            return _am;
        }

>>>>>>> 183db2f33e4be707339b503ea715666e0440a41a
};
#endif // ASSETSMANAGER_H
