owner:external.Shangjun.Zhou@bosch.com

#include <android/binder_manager.h>
#include <thread>
#include <chrono>

// 最大等待 5 秒（与旧 API 行为一致）
static constexpr int kMaxRetryMs = 5000;
static constexpr int kRetryIntervalMs = 250;

AIBinder* getServiceWithTimeout(const std::string& serviceName) {
    auto start = std::chrono::steady_clock::now();

    while (true) {
        AIBinder* binder = AServiceManager_checkService(serviceName.c_str());
        if (binder != nullptr) {
            return binder;
        }

        auto elapsed = std::chrono::steady_clock::now() - start;
        if (std::chrono::duration_cast<std::chrono::milliseconds>(elapsed).count() >= kMaxRetryMs) {
            ALOGE("Timed out waiting for service: %s", serviceName.c_str());
            return nullptr;
        }

        std::this_thread::sleep_for(std::chrono::milliseconds(kRetryIntervalMs));
    }
}

// 替换原来的调用
// 旧: AIBinder *pBinder = AServiceManager_getService(serviceName.c_str());
AIBinder *pBinder = getServiceWithTimeout(serviceName);
if (pBinder == nullptr) {
    ALOGE("Cannot connect to VICS service: %s", serviceName.c_str());
    return STATUS_DEAD_OBJECT;  // 或其他合适的错误码
}


