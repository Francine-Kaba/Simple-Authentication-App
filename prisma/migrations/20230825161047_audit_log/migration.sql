-- CreateTable
CREATE TABLE "audit_log" (
    "id" SERIAL NOT NULL,
    "timestamp" TIMESTAMP(3) NOT NULL DEFAULT CURRENT_TIMESTAMP,
    "userId" INTEGER NOT NULL,
    "action" TEXT NOT NULL,
    "details" TEXT,

    CONSTRAINT "audit_log_pkey" PRIMARY KEY ("id")
);
