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
        AssetsManager( const AssetsManager & _am) = delete;
    public:
        static AssetsManager & getInstance();
        void operator=(const AssetsManager &) = delete;
        std::shared_ptr<sf::Texture> getTexture(std::string _path);

};
#endif // ASSETSMANAGER_H
